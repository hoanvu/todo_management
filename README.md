# Hệ thống quản lí đầu việc

### Cập nhật
+ 22/9/2015: Sử dụng Form và ModelForm cho tất cả form trong project
+ 4/10/2015: Tách các tính năng liên quan tới user: đăng kí, login, logout, ... ra 1 app riêng (<strong>accounts</strong>)

### Giới thiệu
+ Hệ thống này hỗ trợ các tính năng cơ bản nhất để quản lí đầu việc.
+ Sử dụng <strong>Django 1.8</strong> và <strong>Python 2.7.10</strong>
+ Database: <strong>SQLite3</strong>

### Tính năng
Hệ thống bao gồm các tính năng sau:
+ Các tính năng quản lí đầu việc
	+ Hiển thị danh sách các đầu việc chưa làm xong (Đang làm hoặc đang bị hoãn)
	+ Cho phép hiển thị các đầu việc đã xong hoặc đã hủy nếu cần 
	+ Xem chi tiết từng đầu việc
	+ Thay đổi thông tin của đầu việc (trạng thái, độ ưu tiên, ghi chú)
	+ Thêm mới đầu việc

+ Các tính năng về user
	+ Đăng nhập / Đăng xuất
	+ User cần đăng nhập để sử dụng hệ thống, nếu không sẽ hiển thị trang đăng nhập
	+ Thay đổi mật khẩu
	+ Đăng kí tài khoản mới

### Cách sử dụng
Các bạn có thể checkout repo này về và dùng lệnh
```
$ cd todo_management
$ python manage.py runserver
```
để bắt đầu đăng kí tài khoản và sử dụng hệ thống.

### Screenshots
Dưới đây là một số hình ảnh của hệ thống:

![Todo management 1](http://s16.postimg.org/m3wqcen3p/image.jpg)

![Todo management 2](http://s16.postimg.org/hti2gti0l/image.jpg)

![Todo management 3](http://s16.postimg.org/y388jpsol/image.jpg)
