# 5BOYS - Ứng dụng Histogram Equalization

---

## Giới thiệu

- Ứng dụng **Histogram Equalization** là một ứng dụng được xây dựng bằng thư viện (OpenCV), thư viện (numpy) và thư viện (base64), frameword Flask kết hợp với HTML,CSS và JavaScript để tạo giao diện người dùng và thư viện PIL (Pillow) để xứ lý ảnh. Ứng dụng giúp tăng cường độ tương phản của hình ảnh bằng cách thay đổi phân phối của các mức xám.

## Tính năng

- Tải lên hình ảnh: Nhấn nút **"Chọn tệp"** để chọn một hình ảnh từ máy tính của bạn. Hình ảnh đã tải lên sẽ hiển thị trực tiếp trên giao diện.
- Khi nhấn vào nút **"Xử lý"** hình ảnh sẽ được xử lý và hiển thị ra 3 ảnh là: Ảnh gốc - Ảnh Greyscale và Ảnh Tăng độ sáng và cũng như là hiển thị biểu đồ Histogram của Ảnh Greyscale và Ảnh tăng độ sáng.
- Bạn có thể **"kéo thanh tăng giảm độ sáng hoặc nhập giá trị"**. Khi đó Ảnh tăng độ sáng sẽ thay đổi theo và biểu đồ Histogram cũng như thế.
- Bạn có thể nhấn chuột phải vào ảnh hoặc biểu đồ Histogram để có thể tải về.

## Giao diện ứng dụng Histogram Equalization và hướng dẫn sử dụng

1. Giao diện khi người dùng bắt đầu truy cập ứng dụng
   ![z4830997592954_83ab8c56afd3c4124661586d05e88665](https://github.com/Huyhoang23231/HistogramEqualization/assets/96469499/c13700ae-637b-4b12-a069-1318f2f652bb)

)

2. Người dùng nhấn vào nút **"Chọn tệp"** để tiến hành chọn hình và tải lên hình ảnh từ máy tính
   ![z4832498303593_7969d0bc38756734a161140b93ea092d](https://github.com/Huyhoang23231/HistogramEqualization/assets/96469499/d8abc498-bb63-4883-ac41-ae1615b1ca28)


3. Khi tải lên hình ảnh xong người dùng nhấn vào nút **"Xử lý"** để hình ảnh có thể được xử lý và trả về kết quả
   ![Bird - No Brightness](https://github.com/Huyhoang23231/HistogramEqualization/assets/96469499/f0660769-37ed-45aa-a2d9-9c2f162aa15a)


4. Người dùng có thể kéo thanh trượt để có thể tăng giảm độ sáng hoặc nhập vào giá trị (từ 0 - 100)
   ![Bird - Brightness](https://github.com/Huyhoang23231/HistogramEqualization/assets/96469499/0bcdb87f-e0cc-49af-bf04-23b3477cc091)


5. Người dùng có thể nhấn chuột phải vào hình ảnh hoặc biểu đồ chọn **"Lưu hình ảnh thành..."** để có thể tải về
   `Tải về hình ảnh`
   ![download](https://github.com/Huyhoang23231/HistogramEqualization/assets/96469499/6d9eb202-9ad1-453f-ba62-0f1d3b4eedec)

   `Tải về biểu đồ Histogram`
   ![download-chart](https://github.com/Huyhoang23231/HistogramEqualization/assets/96469499/c3f7b7d3-b09f-497b-abfc-8b942b2ed9db)


## Cách ứng dụng Histogram Equalization xử lý ảnh

- **_Bước 1_** (Đọc hình ảnh): Trong bước này, chúng ta đọc hình ảnh gốc bằng cách sử dụng thư viện OpenCV. Hình ảnh gốc sẽ được sử dụng để thực hiện cân bằng biểu đồ.
- **_Bước 2_** (Tính toán Histogram): Chúng ta tính toán histogram của hình ảnh gốc. Histogram là một biểu đồ cho thấy tần suất xuất hiện của các mức xám trong hình ảnh. Nó giúp chúng ta hiểu cách phân phối mức xám trong hình ảnh.
- **_Bước 3_** (Tính toán hàm phân phối tích lũy - CDF): CDF (Cumulative Distribution Function) là một hàm tích lũy của histogram. Nó biểu thị tổng tần suất xuất hiện của các mức xám từ mức xám thấp đến mức xám cao trong hình ảnh. CDF sẽ giúp chúng ta chuyển đổi histogram thành một biểu đồ khác để cân bằng biểu đồ.
- **_Bước 4_** (Chuẩn hóa giá trị CDF): Trong bước này, chúng ta chuẩn hóa giá trị của hàm CDF để đưa chúng về khoảng từ 0 đến 255. Điều này giúp chúng ta tạo ra một ánh xạ giữa các mức xám ban đầu và các mức xám mới.
- **_Bước 5_** (Áp dụng ánh xạ): Sau khi đã có ánh xạ giữa các mức xám ban đầu và các mức xám mới, chúng ta áp dụng ánh xạ này cho hình ảnh gốc. Điều này tạo ra một hình ảnh mới, đã được cân bằng biểu đồ, với độ tương phản cải thiện.
- **_Bước 6_** (Lưu hoặc hiển thị hình ảnh): Cuối cùng, bạn có thể lưu hình ảnh sau khi cân bằng biểu đồ để sử dụng sau này hoặc hiển thị nó trên màn hình. Hình ảnh sau khi cân bằng biểu đồ sẽ có độ tương phản tốt hơn và có thể sử dụng trong các ứng dụng xử lý hình ảnh khác nhau.

---

## Lời Cảm Ơn

Cảm ơn thầy Phan Hồ Viết Trường và Trường Đại học Văn Lang đã tạo điều kiện để nhóm 5BOYS chúng em thực hiện đồ án một cách suôn sẻ. Trong quá trình làm còn nhiều thiếu sót nhưng những lời góp ý và sự giúp đỡ của thầy, nhóm chúng em đã có thể hoàn thành đồ án một cách trọn vẹn.

**Thành viên nhóm 5BOYS**
|STT|Tên thành viên|MSSV|Nhiệm vụ|
|---|--------------|----|--------|
|1|Lê Đức Trung|207CT47990|Nhóm trưởng|
|2|Tạ Huy Hoàng|207CT27868|Thành viên|
|3|Vũ Thanh Phong|207CT40529|Thành viên|
|4|Lê Đình Thiện|207CT28546|Thành viên|
|5|Nguyễn Hữu Trường| 207CT65867|Thành viên|
