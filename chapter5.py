import time

def convert_epoch_time():
    # Lấy tổng số giây từ epoch
    total_seconds = time.time()

    # Tính số ngày kể từ epoch
    days = int(total_seconds // 86400)

    # Tính số giây còn lại của ngày hôm nay
    seconds_remaining = total_seconds % 86400

    # Tính giờ, phút, giây
    hours = int(seconds_remaining // 3600)
    minutes = int((seconds_remaining % 3600) // 60)
    seconds = int(seconds_remaining % 60)

    # In kết quả
    print(f"Số ngày kể từ mốc epoch (1/1/1970): {days} ngày")
    print(f"Thời gian hiện tại (GMT): {hours:02d}:{minutes:02d}:{seconds:02d}")

# Gọi hàm để thực thi
convert_epoch_time()