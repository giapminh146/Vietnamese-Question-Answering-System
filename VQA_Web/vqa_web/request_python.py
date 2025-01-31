import requests
url = "http://127.0.0.1:8000/vqa/"
data = {"context":"Cường Đôla cho biết anh hiện chỉ cao hơn con gái Suchin và con trai Sutin, kém chiều cao bà xã Đàm Thu Trang và con trai riêng 15 tuổi Subeo.", "question":"Cường đô la làm gì?"}
res = requests.post(url=url, json=data)
print(res.json())