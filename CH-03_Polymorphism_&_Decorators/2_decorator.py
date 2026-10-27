def my_decorator(fx):
    def main_func(*args):
        print("before calling the func")
        response= fx(*args)
        #print(response)
        print("after calling the func")
        return response
    return main_func

@my_decorator
def fetch_data(url:str, path:str):
    return f"fetching data from {url} and saving to {path}"

response = fetch_data("https://example.com/data","/tmp/data.csv")
print(response)