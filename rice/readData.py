import pandas as pd
import path

def assert_msg(condition, msg):
    if not condition:
        raise Exception(msg)

def read_file(filename):
    # 获取文件的绝对路径
    filepath = path.join(path.dirname(__file__), filename)

    # 判断文件是否存在
    assert_msg(path.exists(filepath), 'file not exist')

    # 读取CSV文件并返回
    return pd.read_csv(filepath,
                        index_col=0,
                        parse_dates=True,
                        infer_datetime_format=True)

BTCUSD = read_file('BTCUSD_GEMINI.csv')
assert_msg(BTCUSD.__len__() > 0, '读取失败')
print(BTCUSD.head())


# 输入： OHLC数据、初始资金、手续费、交易所类、策略类
# 输出： 最后剩余市值

class Backtest:
    """
    Backtest回测类，用于读取历史行情数据、执行策略、模拟交易并估计收益。
    初始化的时候调用 Backtest.run 来时回调
    instance, or `backtesting.backtesting.Backtest.optimize` to optimize it.
    """
    def __init__(self,
                data: pd.DateFrame,
                strategy_type: type(Strategy),
                broker_type: type(ExchangeAPI),
                cash: float = 10000,
                commission: float = .0):
        """ 
        构造回测对象。需要的参数包括：历史数据，策略对象，初始资金数量，手续费率等。
        初始化过程包括检测输入类型，填充数据空值等。 
        参数： 
        :param data: pd.DataFrame pandas Dataframe格式的历史OHLCV数据 
        :param broker_type: type(ExchangeAPI) 交易所API类型，负责执行买卖操作以及账户状态的维护 
        :param strategy_type: type(Strategy) 策略类型 :param cash: float 初始资金数量 
        :param commission: float 每次交易手续费率。如2%的手续费此处为0.02 
        """
        assert_msg(issubclass(strategy_type, Strategy), 'strategy_type不是一个Strategy类型')
        assert_msg(issubclass(broker_type, ExchangeAPI), 'broker_type不是一个ExchangeAPI类型')
        assert_msg(issubclass(commission, Number), 'commission不是浮点数类型')

        data.copy(False)
        
        # 如果没哟Volumn列，填充NaN
        if 'Volume' not in data:
            data['Volume'] = np.nan

        # 验证OHLC数据格式        
        assert_msg(len(data.columns & {'Open', 'High', 'Low', 'Close', 'Volume'}) == 5,                   
                    ("输入的`data`格式不正确，至少需要包含这些列："                    
                    "'Open', 'High', 'Low', 'Close'"))        
        # 检查缺失值        
        assert_msg(not data[['Open', 'High', 'Low', 'Close']].max().isnull().any(),            
                    ('部分OHLC包含缺失值，请去掉那些行或者通过差值填充. '))        
                    
        # 如果行情数据没有按照时间排序，重新排序一下        
        if not data.index.is_monotonic_increasing:            
            data = data.sort_index()        
        
        # 利用数据，初始化交易所对象和策略对象。        
        self._data = data  # type: pd.DataFrame        
        self._broker = broker_type(data, cash, commission)        
        self._strategy = strategy_type(self._broker, self._data)        
        self._results = None

    def run(self):
        """
        运行回测， 迭代历史数据，执行模拟交易并返回回测结果。
        """
        strategy = self._strategy
        broker = self._broker

        # 策略初始化
        strategy.init()

        # 设定回测开始时间和结束位置
        start = 100
        end = len(self._data)

        # 回测主循环，更新市场状态，然后执行策略
        for i in range(start, end):
            broker.next(i)
            strategy.next(i)
        
        # 完成策略执行之后，计算结果并返回
        self._results = self._compute_result(broker)
        return self._results

    def _compute_result(self, broker):
        s = pd.Series()
        s['初始市值'] = broker.initial_cash
        s['结束市值'] = broker.market_value
        s['收益'] = broker.market_value - broker.initial_cash
        return s
    
    
        


