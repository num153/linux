 #!/bin/bash

echo "Nhap ten cua ban"
read ten
echo "Nhap nam sinh"
read nam

namHienTai=$(date +%Y)
tuoi=$((namHienTai-nam))
echo "Nam hien tai la $namHienTai va ban dang $tuoi"
