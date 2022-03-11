def func_counter(func):
        
        def wrapper(x):
            
            func(x)
            wrapper.counter = wrapper.counter + 1
            
        wrapper.counter = 0 
        return wrapper
