import os
import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import tkinter.simpledialog as sd
import datetime


tk.Tk().withdraw()


# プロジェクト名の記載
def project_name_description():
    project_name = sd.askstring("プロジェクト名を入力","プロジェクト名を入力してください。\nディレクトリ名に利用します。")
    return project_name


# 作成するディレクトリ名
def create_directory_name():
    today = datetime.datetime.now().strftime("%Y%m%d")
    project_name = project_name_description()
    directory_names = [
        "接続情報",
        "契約資料",
        today+"_"+project_name,
        [
            "提案・見積り",
            "スケジュール・QA・議事録",
            [
                "過去QA",
                "議事録"
            ],
            "受領",
            "成果物",
            [
                "納品物",
                "納品物以外"
            ],
            "作業ログ",
            "99.その他資料"
        ]
    ]
    return directory_names


# ディレクトリの選択
def select_directory():
    filepath = fd.askdirectory(
        title="フォルダを作成するディレクトリを選択する",
        initialdir = "C:"
    )
    return filepath


# def array_processing_directory(n):
#     if isinstance(n, list):
#         for i in n:
            


# ディレクトリの作成
def create_directory():
    # try:
    directory_name = create_directory_name()
    filepath = select_directory()
    # os.makedirs(filepath + "/" + i)
    for i in directory_name:
        # os.mkdir(i)
        if isinstance(i, list):
            for j in i:
                if isinstance(j, list):
                    for k in j:
                        print((filepath + "/" + str(i) + "/" + str(j) + "/" + str(k)))
                else:
                    print((filepath + "/" + str(i) + "/" + str(j)))
        else:
            # print("i"+str(i))
            print((filepath + "/" + str(i)))
    # except:
    #     mb.showinfo("エラー","対象ファイル名が既に存在している可能性があります。\n不明箇所は開発者に問合せください。")


if __name__ == '__main__':
    create_directory()


