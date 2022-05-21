import os
import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import tkinter.simpledialog as sd
import datetime
import sys
import traceback


tk.Tk().withdraw()


# プロジェクト名の記載
def project_name_description():
    project_name = sd.askstring("プロジェクト名を入力", "プロジェクト名を入力してください。\nディレクトリ名に利用します。")
    return project_name


# 作成するディレクトリ名
def create_directory_name():
    today = datetime.datetime.now().strftime("%Y%m%d")
    project_name = project_name_description()
    if project_name is None:
        sys.exit()  # ディレクトリ選択画面でキャンセル選択
    if project_name == "":
        mb.showinfo("警告", "プロジェクト名を選択してください")  # プロジェクト名が未記載だった場合
        create_directory_name()
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
        initialdir="C:"
    )
    print(filepath)
    if filepath == "" or filepath is None:
        sys.exit()  # ファイルパスの選択でキャンセス
    return filepath


# ディレクトリの作成
def create_directory():
    try:
        directory_names = create_directory_name()
        filepath = select_directory()
        for i in directory_names:
            if not isinstance(i, list):
                d_i = i
            if isinstance(i, list):
                for j in i:
                    if not isinstance(j, list):
                        d_j = j
                    if isinstance(j, list):
                        for k in j:
                            os.makedirs(filepath + "/" + str(d_i) + "/" + str(d_j) + "/" + str(k), exist_ok=False)
                    else:
                        os.makedirs(filepath + "/" + str(d_i) + "/" + str(d_j), exist_ok=False)
            else:
                os.makedirs(filepath + "/" + str(d_i), exist_ok=False)
        fd.askopenfilename(initialdir=filepath)
    except Exception as e:
        mb.showinfo("エラー", str(e))
        print(traceback.format_exc())


if __name__ == '__main__':
    create_directory()
