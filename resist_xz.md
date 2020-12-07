# resist_xz

瞎寫的。

:heavy_exclamation_mark: 沒用數據庫。

:heavy_exclamation_mark: 沒有區分“蕭戰方實錘”、“個人行動”、“對蕭戰方的態度”。

:negative_squared_cross_mark: 代碼寫得不是很聰明的樣子。

:label: 目前tag權重全隨機。

:small_blue_diamond: 暫時沒出現“重複微博”的情況。



`[r]`: 根據<u>sentence_test.txt</u> 裡的內容把 <u>sentence.txt</u> & <u>tag.txt</u> 全部*抹掉重寫*。

`[w]`: 隨機抓取兩個tag、三個句子以及表情符號拼在一起並放在系統的剪貼板上。

`[c]`: 每兩秒生成一條帶tag和表情符號的微博，並放在剪貼板上以供發布新微博。剪貼板上的內容每2s刷新一次、共刷新32次。<!--這種情況適合與連續發微博，只需要粘貼、發送即可。-->

`[q]`: 停止運行。



