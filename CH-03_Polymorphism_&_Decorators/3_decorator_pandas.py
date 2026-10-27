def pandas_decorator(fx):
    def main_func(*args):
        response = fx(*args)
        response.to_parquet("CH-03_Polymorphism_&_Decorators/temp.parquet")
        return response
    return main_func

@pandas_decorator
def csv_to_parquet(file_path:str):
    import pandas as pd
    df= pd.read_csv(file_path)
    return 


response = csv_to_parquet("CH-03_Polymorphism_&_Decorators/orders.csv")
print(response.head())
