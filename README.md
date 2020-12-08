# resist_xz

瞎寫的。

:heavy_exclamation_mark: 沒用數據庫。

:heavy_exclamation_mark: 沒有區分“蕭戰方實錘”、“個人行動”、“對蕭戰方的態度”。

:negative_squared_cross_mark: 代碼寫得不是很聰明的樣子。

:label: 目前tag權重全隨機。

:small_blue_diamond: 暫時沒出現“重複微博”的情況。



`[r]`: 根據<u>sentence_test.txt</u> 裡的內容把 <u>sentence.txt</u> & <u>tag.txt</u> 全部*抹掉重寫*。

`[w]`: 隨機抓取兩個tag、三個句子以及表情符號拼在一起並放在系統的剪貼板上。

`[c]`: 每兩秒生成一條帶tag和表情符號的微博，並放在剪貼板上以供發布新微博。剪貼板上的內容每2s刷新一次、共刷新32次。（這種情況適合與連續發微博，只需要粘貼、發送即可。）

`[q]`: 停止運行。



***

*短打教程*

1. 確保電腦上有python環境（官網好像最近有3.9了，不過3.8肯定OK）。
2. 然後用pip / conda / PyCharm裝一個pyperclip吧，挺小的。
3. 把sentece.txt & tag.txt & test.py 一共三個文件下載後放在同一個文件夾裡。
4. 用python運行 test.py 文件。
5. 輸入 `w / c / q` 。（一般情況不必輸入`r`，如果誤操作的話，推薦重新下載sentece.txt & tag.txt 覆蓋本地的這倆文件。）
6. 如果有加入第三個熱點tag （比如： `#肖战一键换装#`），用记事本打开.py文件找到第7行替换tag即可；如果无第三个热点tag的需求，把第七行改成`append_tag = ""`即可。
7. 食用愉快～一起给🈹️🈹️艸数据呀～