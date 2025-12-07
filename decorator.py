# 1. Write a function that appends 1 to 1000 numbers to a list and add a decorator to that function to calculate the start and end time.
# Calculate the total time taken and print.
import time

from week_2.lamda_map_filter_reduce import result


def time_calculator(func):
    def wrapper(* args, ** kwargs):
        start = time.time()
        result = func(* args, ** kwargs)
        end = time.time()
        print(f"time taken : {end-start}")
        return result
    return wrapper
@time_calculator
def appender(x):
    ls = []
    ans = 0
    for i in range (x):
        ans += i
    return ans

print(appender(1000))
# 2. Create a parameterised decorator retry that retries a function a specified number of times.
#
def retry(x):
    def decorator(func):
        def wrapper(* args, ** kwargs):
            for i in range (x):
                func(*args, **kwargs)
        return wrapper
    return decorator

@retry(3)
def may_fail(name):
    print(f"Hello, {name}!")

may_fail("Avi")
#
# 3. Create a decorator validate_positive for below function that ensures the argument passed to a function is positive.
#
def validate_positive(func):
    def wrapper(*args, **kwargs):
        result = 0;
        for x in list(args):
            if(x < 0):
                print("negative argument passed")
            else:
                result = func(*args,**kwargs)
        return result
    return wrapper

@validate_positive
def square_root(x):
    return x ** 0.5

print(square_root(1))
print(square_root(-1))

# 4. Create a decorator cache that caches the result of a function based on its arguments.
# Write a cache decorator for it to check if the calculation is already performed then return the result.

d = {}
def cache(func):
    def wrapper(* args, **kwargs):
        k = args[0]
        if k in d:
            return d[k]
        result = func(*args, **kwargs)
        d[k] = result
        return result
    return wrapper

@cache
def expensive_computation(x):
    print("Performing computation...")
    return x * x

print(expensive_computation(5))
print(expensive_computation(5))

# 5. Create a decorator requires_permission that checks if a user has the ‘admin’ permission before allowing access to a function, if a different user then responds “Access denied”.
#
def requires_permission(func):
    def wrapper(user, *args, **kwargs):
        if 'admin' in user.get('permissions', []):
            func(user, *args, **kwargs)
        else:
            print("Admin permission needed!!!")
    return wrapper

@requires_permission
def delete_user(user, user_id):
    print(f"User {user_id} deleted by {user['name']}")

user1 = {'name': 'Alice', 'permissions': ['admin']}
user2 = {'name': 'John', 'permissions': ['dev']}
user3 = {'name': 'Kurt', 'permissions': ['test']}
delete_user(user1, user2)
delete_user(user3, user2)
