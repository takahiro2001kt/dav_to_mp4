import os
import subprocess
import time

totalstart = time.time()

# 入力フォルダと出力フォルダを定義
input_folder = '/Users/takahiro/Desktop/testdata'
output_folder = '/Users/takahiro/Desktop/savedata'

# 出力フォルダが存在しない場合は作成
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# 入力フォルダ内の全ファイルを走査
for file in os.listdir(input_folder):
    start = time.time()
    if file.endswith('.dav'):
        # 入力ファイルと出力ファイルのパスを設定
        input_file = os.path.join(input_folder, file)
        output_file = os.path.join(output_folder, file.replace('.dav', '.mp4'))

        # ffmpeg コマンドを使用してファイルを変換
        print(f"{file} is currently under conversion")
        command = ['ffmpeg', '-i', input_file, output_file]
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    end = time.time()
    print(f"{file} - FINISH CONVERSION")
    print(f"TIME : {(end - start)/60}","\n")

totalend = time.time()
print("-----FULL CONVERT from DAV to MP4-----")
print(f"TOTAL TIME : {(totalend - totalstart)/60}")


