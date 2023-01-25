def find_lingerie(size_it: str) -> dict:
    lingerie = {"XXS": {"DEU": "34-36", "RUS": "40-42", "USA": "8", "FRA": "38", "GBR": "24"},
                "XS": {"DEU": "38", "RUS": "44", "USA": "10", "FRA": "40", "GBR": "26"},
                "S": {"DEU": "40", "RUS": "46", "USA": "12", "FRA": "42", "GBR": "28"},
                "M": {"DEU": "42", "RUS": "48", "USA": "14", "FRA": "44", "GBR": "30"},
                "L": {"DEU": "44", "RUS": "50", "USA": "16", "FRA": "46", "GBR": "32"},
                "XL": {"DEU": "46", "RUS": "52", "USA": "18", "FRA": "48", "GBR": "34"},
                "XXL": {"DEU": "48", "RUS": "54", "USA": "20", "FRA": "50", "GBR": "36"},
                "XXXL": {"DEU": "50", "RUS": "56", "USA": "22", "FRA": "52", "GBR": "38"}}
    for k, v in lingerie.items():
        if str(size_it) == k:
            return v

while True:
    size_it = input("Wrtite your internetional size: ")
    if len(size_it) <= 4 and len(size_it) > 0:
        print(find_lingerie(size_it))
    else:
        print("This is not size of lingerie!!!")
    ext = input("Write 1 for exit: ")
    if ext == "1":
        break
