## 2023 軟體開發技能複習計劃

為了讓好不容易獲得的新知徹底遺忘復習是最佳的手段！

不管，你是使用 [遺忘曲線](https://zh.wikipedia.org/zh-tw/%E9%81%97%E5%BF%98%E6%9B%B2%E7%BA%BF) | [參考資料](https://www.youtube.com/watch?v=zbu9WBAZCZE)
還是各種的學習理論，要把學過的東西再次掌握，就是得在那個要忘不忘的時刻來做才會效果顯著！。

這回合要復習的主要內容是來自《水球軟體學院的遊戲微服務計劃》線上讀書會的相關內容，過去的資料可以參考 [動機篇](docs/motivation.md)。

## 複習進度

相關進度的 YouTube 記錄如下：

| 場次    | 摘要                                                                                                        |
|-------|-----------------------------------------------------------------------------------------------------------|
| 第一回   | [簡單看一下遊戲介紹](https://www.youtube.com/watch?v=b-lr7aRmjBg)                                                  |
| 第二回   | [蒐集遊戲規則, 並精簡出一版文字規則](https://www.youtube.com/watch?v=4NnSTflmih0)                                         |
| 第三回   | [蒐集遊戲卡牌資訊, 並整理佈局資料](https://www.youtube.com/watch?v=JQFVOQ8LNTM)                                          |
| 第四回   | [Event Storming](https://www.youtube.com/watch?v=eZeaLqyz1ss)                                             |
| 第五回   | [加上 Command 與 Rule](https://www.youtube.com/watch?v=dUl3J6j8UrU)                                          |
| 第五點五回 | [中場回顧](https://www.youtube.com/watch?v=sdTWeMaCuvU)                                                       |
| 第六回   | OOA [6-1](https://www.youtube.com/watch?v=HfZJAue0ioc)、[6-2](https://www.youtube.com/watch?v=t-MaN5L8qsA) | 
| 第七回   | Walking Skeleton (ongoing)                                                                                |
| 第八回   | ATDD (ongoing)                                                                                            |

### 5/2 中場回顧

趁著連假推了一下進度，把遊戲規則大致上看了，也找先畫了一條 Happy Path：遊戲開始、所有玩家都拿到了需要的東西，桌面也佈置完成，直到某一位玩家贏得角色。

儘可能走輕量化的 Event Storming 流程，所以大致上在二次內搞定，第 1 次找 Domain Event，第 2 次弄 Command 與
Rule。其它就先忽略，後面有需要再補就好。

接著，可能做一些 OOA 的開頭，再來弄點不太需要有 Domain Knowledge 的 Walking Skeleton，有了基礎建設後就可以來做 ATDD 與
Example Mapping 囉！Example Mapping 同樣是有用到才討論，ATDD 戰霧開到哪 Example Mapping 才做到那邊。