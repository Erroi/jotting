function func(message) {
    function get_message(message){
        console.log('message:', message)
    }
    return get_message
    // return get_message(message)
}

func()('hello')
// func('hello')