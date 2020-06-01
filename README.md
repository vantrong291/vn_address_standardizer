# Bộ chuẩn hóa  địa chỉ Việt Nam (English below)
A package for parsing Vietnamese address


## Tính năng
1. Xử lỹ những tên viết tắt thông dụng
2. Sửa chính tả
3. Sửa lỗi thứ tự tên đơn vị hành chính
4. Thêm prefix (xã, huyện, tỉnh, ...)


## Cài đặt qua PyPi
```shell
pip3 install vnaddress
```

## Testing
```python

from vnaddress import VNAddressStandardizer

address = VNAddressStandardizer(raw_address = "Dicjh Vongj Haaju", comma_handle = True)
address.execute()

# output
# phường Dịch Vọng Hậu, quận Cầu Giấy, thành phố Hà Nội


address = VNAddressStandardizer(raw_address = "Dicjh Vongj Haaju, ", comma_handle = True, detail=True)
address.execute()

# output
# {'result': 'phường Dịch Vọng Hậu, quận Cầu Giấy, thành phố Hà Nội', 'match': {'match_address': 'Dịch Vọng Hậu, Cầu Giấy, Hà Nội', 'match_percent': 100}, 'missing': ['TTP', 'QH'], 'detail': {'PX': 'Dịch Vọng Hậu', 'QH': 'Cầu Giấy', 'TTP': 'Hà Nội'}}

```
------------------------------------------
## [English]
## Features
1. Handling common abbreviations
2. Edit the spelling
3. Correct the order of administrative unit names
4. Add prefix (commune, district, province, ...)


## Install via PyPi
```shell
pip3 install vnaddress
```

## Testing
```python

from vnaddress import VNAddressStandardizer

address = VNAddressStandardizer(raw_address = "Dicjh Vongj Haaju", comma_handle = True)
address.execute()

# output
# phường Dịch Vọng Hậu, quận Cầu Giấy, thành phố Hà Nội


address = VNAddressStandardizer(raw_address = "Dicjh Vongj Haaju, ", comma_handle = True, detail=True)
address.execute()

# output
# {'result': 'phường Dịch Vọng Hậu, quận Cầu Giấy, thành phố Hà Nội', 'match': {'match_address': 'Dịch Vọng Hậu, Cầu Giấy, Hà Nội', 'match_percent': 100}, 'missing': ['TTP', 'QH'], 'detail': {'PX': 'Dịch Vọng Hậu', 'QH': 'Cầu Giấy', 'TTP': 'Hà Nội'}}

```
