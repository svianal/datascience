from prefect import flow
from task.extract import extract
from task.transform import transform
from task.load import  load

@flow
def main():
    data = extract()
    data_transform = transform(data)
    load(data_transform)
    
if __name__ == "__main__":
    main()