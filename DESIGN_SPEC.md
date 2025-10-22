# Mouse Rover - 設計規格文檔 (Design Specification)

> 本文檔提供完整的設計系統規格，方便設計師在 Figma 或其他設計工具中實現

## 目錄
- [設計理念](#設計理念)
- [色彩系統](#色彩系統)
- [字體系統](#字體系統)
- [間距系統](#間距系統)
- [組件庫](#組件庫)
- [佈局規格](#佈局規格)
- [互動設計](#互動設計)
- [響應式設計](#響應式設計)
- [Figma 實作指南](#figma-實作指南)

---

## 設計理念

### 核心價值
- **直觀易懂**：使用者能立即理解工具的功能和運作方式
- **視覺化呈現**：透過互動式畫布展示抽象的程式邏輯
- **專業感**：採用現代化的漸層設計和流暢動畫
- **可玩性**：提供互動體驗，讓使用者能實際操作測試

### 設計風格
- **現代扁平設計** (Modern Flat Design)
- **漸層色彩** (Gradient Colors)
- **圓角元素** (Rounded Corners)
- **陰影層次** (Layered Shadows)
- **流暢動畫** (Smooth Animations)

---

## 色彩系統

### 主色調 (Primary Colors)

#### 品牌漸層
```
Gradient: 135deg
- Start: #667eea (紫藍色)
- End: #764ba2 (深紫色)

用途：
- 頁面主要背景
- Header 區域
- 主要按鈕 (CTA)
- 重要標題
```

#### 品牌單色
```
Primary: #667eea
用途：
- 連結
- 圖標
- 滑桿 thumb
- 數值顯示
```

### 輔助色彩 (Secondary Colors)

#### 功能色
```
成功 (Success): #28a745
- 用途：啟動狀態、自動移動指示器

資訊 (Info): #007bff
- 用途：使用者操作指示器

警告 (Warning): #ffc107
- 用途：警告提示

危險 (Danger): #dc3545
- 用途：停止按鈕、Hot Corner 邊界
```

#### 中性色
```
白色 (White): #ffffff
灰色階：
- Gray 50: #f8f9fa (卡片背景)
- Gray 100: #e9ecef (按鈕背景)
- Gray 200: #dee2e6 (邊框)
- Gray 300: #ced4da
- Gray 400: #adb5bd
- Gray 500: #6c757d (輔助文字)
- Gray 600: #495057 (次要文字)
- Gray 700: #343a40
- Gray 800: #212529
- Gray 900: #1e1e1e (日誌背景)

黑色 (Black): #000000
```

### 背景色
```
主背景漸層：
linear-gradient(135deg, #667eea 0%, #764ba2 100%)

卡片背景：#f8f9fa
白色容器：#ffffff
日誌背景：#1e1e1e
資訊框背景：#e7f3ff
命令框背景：#2d2d2d
```

### 色彩使用規範

#### 對比度要求
- 文字與背景對比度至少 4.5:1 (WCAG AA)
- 大文字（18pt+）對比度至少 3:1
- 互動元素對比度至少 3:1

#### 色彩情境使用
| 情境 | 色彩 | 用途 |
|------|------|------|
| 程式自動移動 | #28a745 (綠) | 視覺化畫布上的自動移動點 |
| 使用者操作 | #007bff (藍) | 使用者點擊的位置 |
| 初始狀態 | #6c757d (灰) | 未開始時的指示器 |
| Hot Corner | #dc3545 (紅) | 危險區域標示 |

---

## 字體系統

### 字體家族 (Font Family)

#### 主要字體
```css
font-family: -apple-system, BlinkMacSystemFont,
             'Segoe UI', 'Roboto', 'Oxygen',
             'Ubuntu', 'Cantarell', sans-serif;
```

#### 等寬字體 (Monospace)
```css
font-family: 'Courier New', 'Monaco', monospace;

用途：
- 程式碼顯示
- 命令列
- 日誌輸出
- 座標數值
```

### 字體大小 (Font Sizes)

```
特大標題 (Hero): 48px (3em)
- 用途：主頁面標題

大標題 (H1): 30px (1.875em)
- 用途：區域標題

中標題 (H2): 24px (1.5em)
- 用途：卡片標題

小標題 (H3): 19.2px (1.2em)
- 用途：子標題、Header 副標題

正文 (Body): 16px (1em)
- 用途：一般內容、按鈕文字

小文字 (Small): 14.4px (0.9em)
- 用途：說明文字、日誌

微小文字 (Tiny): 13.6px (0.85em)
- 用途：標籤、提示
```

### 字體粗細 (Font Weights)

```
Regular: 400
- 用途：正文、說明

Semi-Bold: 600
- 用途：標籤、重要資訊

Bold: 700
- 用途：標題、數值顯示
```

### 行高 (Line Height)

```
標題: 1.2
正文: 1.5
日誌: 1.5
按鈕: 1
```

### 字元間距 (Letter Spacing)

```
標題: 正常 (0)
正文: 正常 (0)
按鈕: 0.5px (大寫時)
```

---

## 間距系統

### 間距比例 (Spacing Scale)

採用 8px 基準的間距系統：

```
4px  (0.25rem) - 極小間距
8px  (0.5rem)  - 小間距
12px (0.75rem) -
16px (1rem)    - 基準間距
20px (1.25rem) -
24px (1.5rem)  - 中等間距
32px (2rem)    -
40px (2.5rem)  - 大間距
48px (3rem)    -
64px (4rem)    - 超大間距
```

### 元件內部間距 (Padding)

```
按鈕 (Button):
- 垂直: 15px
- 水平: 30px

卡片 (Card):
- 全方向: 25px

控制組 (Control Group):
- 底部邊距: 25px

資訊框 (Info Box):
- 全方向: 15px

日誌容器 (Log Container):
- 全方向: 20px

Header:
- 全方向: 40px
```

### 元件外部間距 (Margin)

```
卡片之間: 30px
控制組之間: 25px
標題下方: 20px
標籤下方: 8px
區域內容: 40px
```

### 網格系統 (Grid)

```
主要佈局:
display: grid
grid-template-columns: 1fr 1fr
gap: 30px

統計卡片:
display: grid
grid-template-columns: repeat(2, 1fr)
gap: 15px
```

---

## 組件庫

### 1. 按鈕 (Buttons)

#### 主要按鈕 (Primary Button)
```
尺寸:
- 高度: 50px (padding: 15px 30px)
- 最小寬度: flex: 1 (彈性寬度)

樣式:
- 背景: linear-gradient(135deg, #667eea 0%, #764ba2 100%)
- 文字顏色: #ffffff
- 圓角: 10px
- 字體大小: 16px (1em)
- 字重: 600
- 邊框: none
- 陰影: none (正常), 0 6px 20px rgba(102, 126, 234, 0.4) (hover)

狀態:
- Normal: 原始樣式
- Hover: transform: translateY(-2px) + 陰影
- Active: transform: translateY(0)
- Disabled: opacity: 0.6, cursor: not-allowed

文字: ▶️ 開始演示
```

#### 次要按鈕 (Secondary Button)
```
尺寸: 同主要按鈕

樣式:
- 背景: #e9ecef
- 文字顏色: #495057
- 其他同主要按鈕

狀態:
- Hover: background: #dee2e6

文字: 🔄 重置
```

#### 危險按鈕 (Danger Button)
```
尺寸: 同主要按鈕

樣式:
- 背景: #dc3545
- 文字顏色: #ffffff
- 其他同主要按鈕

狀態:
- Hover: background: #c82333

文字: ⏹️ 停止演示
```

#### 小型按鈕 (Small Button - 複製按鈕)
```
尺寸:
- padding: 5px 10px

樣式:
- 背景: #667eea
- 文字顏色: #ffffff
- 圓角: 5px
- 字體大小: 12.8px (0.8em)

狀態:
- Hover: background: #5568d3
```

### 2. 卡片 (Cards)

#### 標準卡片
```
尺寸:
- 寬度: 自適應容器
- padding: 25px

樣式:
- 背景: #f8f9fa
- 圓角: 15px
- 陰影: 0 4px 6px rgba(0,0,0,0.07)

內容結構:
- 標題 (H2): margin-bottom: 20px
- 內容區域
```

#### 統計卡片 (Stat Card)
```
尺寸:
- padding: 15px

樣式:
- 背景: #ffffff
- 圓角: 10px
- 邊框: 2px solid #e9ecef
- 文字對齊: center

內容結構:
- 數值 (stat-value):
  - 字體大小: 32px (2em)
  - 字重: 700
  - 顏色: #667eea
  - display: block

- 標籤 (stat-label):
  - 顏色: #6c757d
  - 字體大小: 14.4px (0.9em)
  - margin-top: 5px
```

### 3. 表單控制項 (Form Controls)

#### 滑桿 (Range Slider)
```
尺寸:
- 寬度: 100%
- 高度: 6px

軌道 (Track):
- 背景: #ddd
- 圓角: 3px

滑塊 (Thumb):
- 寬度: 20px
- 高度: 20px
- 圓角: 50% (圓形)
- 背景: #667eea
- 陰影: 0 2px 4px rgba(0,0,0,0.2)
- cursor: pointer

狀態:
- Hover: 略微放大
- Active: 陰影加深
```

#### 開關按鈕 (Toggle Switch)
```
容器:
- 寬度: 60px
- 高度: 34px
- 位置: relative

滑塊背景:
- 圓角: 34px (完全圓角)
- 背景: #ccc (未選中), #667eea (選中)
- 過渡: 0.4s

滑塊圓點:
- 尺寸: 26px x 26px
- 圓角: 50%
- 背景: #ffffff
- 位置: left: 4px, bottom: 4px
- 過渡: 0.4s
- 選中位移: translateX(26px)
```

#### 數值顯示標籤
```
樣式:
- display: inline-block
- 背景: #667eea
- 文字顏色: #ffffff
- padding: 4px 12px
- 圓角: 20px (膠囊形)
- 字重: 600
- margin-left: 10px
```

### 4. 資訊框 (Info Boxes)

#### 標準資訊框
```
樣式:
- 背景: #e7f3ff
- 左邊框: 4px solid #667eea
- padding: 15px
- 圓角: 5px
- margin-top: 15px

文字:
- 強調文字 (<strong>): color: #667eea
```

#### 命令框 (Command Box)
```
樣式:
- 背景: #2d2d2d
- 文字顏色: #f8f8f2
- padding: 15px
- 圓角: 8px
- font-family: 'Courier New', monospace
- 位置: relative

程式碼文字:
- 顏色: #a6e22e

複製按鈕:
- 位置: absolute, top: 10px, right: 10px
```

### 5. 日誌容器 (Log Container)

```
尺寸:
- max-height: 250px
- overflow-y: auto

樣式:
- 背景: #1e1e1e
- 文字顏色: #d4d4d4
- padding: 20px
- 圓角: 10px
- font-family: 'Courier New', monospace
- 字體大小: 14.4px (0.9em)

日誌條目:
- margin-bottom: 8px
- line-height: 1.5

顏色標記:
- timestamp: #4ec9b0 (青綠色)
- mouse emoji: #ce9178 (橙色)
- position: #dcdcaa (黃色)
```

### 6. 畫布 (Canvas)

```
尺寸:
- 寬度: 100%
- 高度: 500px

樣式:
- 邊框: 3px solid #667eea
- 圓角: 15px
- cursor: crosshair
- display: block

容器:
- 背景: #ffffff
- 圓角: 15px
- 陰影: 0 4px 6px rgba(0,0,0,0.07)
- overflow: hidden

Hot Corner 標記:
- 樣式: 虛線
- 顏色: #dc3545
- 線寬: 2px
- 虛線樣式: [5, 5]
```

---

## 佈局規格

### 整體容器 (Container)

```
最大寬度: 1400px
邊距: 0 auto (居中)
背景: #ffffff
圓角: 20px
陰影: 0 20px 60px rgba(0,0,0,0.3)
溢出: hidden
```

### Header 區域

```
佈局:
- padding: 40px
- text-align: center

背景:
- linear-gradient(135deg, #667eea 0%, #764ba2 100%)

標題 (H1):
- 字體大小: 48px (3em)
- margin-bottom: 10px
- 字重: 700
- 顏色: #ffffff

副標題 (p):
- 字體大小: 19.2px (1.2em)
- 透明度: 0.9
- 顏色: #ffffff
```

### 主要內容區 (Content)

```
佈局:
display: grid
grid-template-columns: 1fr 1fr
gap: 30px
padding: 40px

響應式斷點:
@media (max-width: 1024px) {
  grid-template-columns: 1fr
}
```

### 左側面板 (Left Panel)

```
佈局:
display: flex
flex-direction: column
gap: 30px

包含:
1. 控制面板卡片
2. 統計資訊卡片
3. 活動日誌卡片
```

### 右側面板 (Right Panel)

```
包含:
1. 視覺化畫布卡片
```

---

## 互動設計

### 按鈕互動

#### 主要按鈕懸停效果
```css
transition: all 0.3s ease

Hover 狀態:
- transform: translateY(-2px)
- box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4)

Active 狀態:
- transform: translateY(0)
```

#### 按鈕狀態管理
```
開始按鈕:
- 運行時: disabled = true
- 停止時: disabled = false

停止按鈕:
- 運行時: disabled = false
- 停止時: disabled = true
```

### 滑桿互動

```
Input 事件:
- 即時更新數值顯示
- 即時更新命令顯示
```

### 開關按鈕互動

```
切換動畫:
- 背景顏色過渡: 0.4s
- 圓點位移過渡: 0.4s

Change 事件:
- 更新命令顯示
```

### 畫布互動

#### 點擊事件
```
功能: 模擬使用者移動滑鼠

視覺回饋:
1. 清除畫布
2. 重繪 Hot Corner 邊界
3. 在點擊位置繪製藍色圓圈
4. 添加標籤 "👆"
5. 更新座標顯示
6. 添加日誌記錄
```

#### 自動移動視覺化
```
顯示元素:
1. 綠色圓圈 (半徑: 8px)
2. 白色邊框 (寬度: 2px)
3. 文字標籤 "🐱"
```

### 日誌滾動

```
行為:
- 新日誌添加時自動滾動到底部
- scrollTop = scrollHeight
```

### 複製按鈕

```
點擊效果:
1. 複製命令到剪貼簿
2. 按鈕文字改為 "已複製!"
3. 2秒後恢復原文字 "複製"
```

---

## 響應式設計

### 斷點 (Breakpoints)

```
Desktop: > 1024px
- 雙欄佈局
- 完整功能顯示

Tablet/Mobile: ≤ 1024px
- 單欄佈局
- grid-template-columns: 1fr
```

### 移動端優化

```
Container padding:
- Desktop: 20px
- Mobile: 10px

Header padding:
- Desktop: 40px
- Mobile: 20px

字體縮放:
- 使用 rem 單位
- 基準字體: 16px

觸控目標:
- 最小尺寸: 44x44px (iOS 標準)
- 按鈕高度: 50px
- 開關按鈕: 60x34px
```

---

## Figma 實作指南

### 1. 設置 Figma 文件

#### 畫布設置
```
Frame Name: Mouse Rover Demo
Width: 1400px
Height: Auto

Background:
- Fill: Linear Gradient
- Angle: 135°
- Color 1: #667eea (0%)
- Color 2: #764ba2 (100%)
```

#### 網格設置
```
Layout Grid:
- Type: Columns
- Count: 12
- Margin: 40px
- Gutter: 30px

另一個 Layout Grid:
- Type: Rows
- Height: 8px (基準間距)
```

### 2. 建立色彩樣式 (Color Styles)

建立以下色彩樣式：

```
Primary/Gradient - 漸層
Primary/Solid - #667eea
Success - #28a745
Info - #007bff
Warning - #ffc107
Danger - #dc3545

Gray/50 - #f8f9fa
Gray/100 - #e9ecef
Gray/500 - #6c757d
Gray/600 - #495057
Gray/900 - #1e1e1e

Background/Card - #f8f9fa
Background/Info - #e7f3ff
Background/Command - #2d2d2d
Background/Log - #1e1e1e

Text/Primary - #333333
Text/Secondary - #6c757d
Text/White - #ffffff
```

### 3. 建立文字樣式 (Text Styles)

```
Heading/Hero
- Font: System (San Francisco/Segoe UI)
- Size: 48px
- Weight: Bold (700)
- Line Height: 1.2

Heading/H1
- Size: 30px
- Weight: Bold (700)

Heading/H2
- Size: 24px
- Weight: Bold (700)

Body/Regular
- Size: 16px
- Weight: Regular (400)
- Line Height: 1.5

Body/Semibold
- Size: 16px
- Weight: Semibold (600)

Caption
- Size: 14px
- Weight: Regular (400)

Code
- Font: Courier New
- Size: 14px
- Weight: Regular (400)
- Line Height: 1.5
```

### 4. 建立效果樣式 (Effect Styles)

```
Shadow/Card
- Type: Drop Shadow
- X: 0, Y: 4px
- Blur: 6px
- Color: #000000, Opacity: 7%

Shadow/Container
- Type: Drop Shadow
- X: 0, Y: 20px
- Blur: 60px
- Color: #000000, Opacity: 30%

Shadow/Button Hover
- Type: Drop Shadow
- X: 0, Y: 6px
- Blur: 20px
- Color: #667eea, Opacity: 40%
```

### 5. 建立組件 (Components)

#### 按鈕組件

```
Component Set Name: Button

Variants:
1. Type: Primary, State: Default
2. Type: Primary, State: Hover
3. Type: Primary, State: Disabled
4. Type: Secondary, State: Default
5. Type: Secondary, State: Hover
6. Type: Danger, State: Default
7. Type: Danger, State: Hover

Properties:
- Type: Primary | Secondary | Danger
- State: Default | Hover | Disabled
- Icon: Boolean (顯示/隱藏 emoji)
- Label: Text
```

#### 卡片組件

```
Component Name: Card

Structure:
- Container (Auto Layout, Vertical)
  - Title (Text)
  - Content Slot (Component Slot)

Properties:
- Title: Text
- Padding: 25px
- Border Radius: 15px
- Background: Gray/50
```

#### 統計卡片組件

```
Component Name: Stat Card

Structure:
- Container (Auto Layout, Vertical)
  - Value (Text, Large)
  - Label (Text, Small)

Properties:
- Value: Text
- Label: Text
```

#### 滑桿組件

```
Component Set Name: Slider

Variants:
1. State: Default
2. State: Hover
3. State: Active

包含:
- Track (Rectangle, 6px height)
- Thumb (Circle, 20px diameter)
- Value Display (Label component)
```

#### 開關組件

```
Component Set Name: Toggle

Variants:
1. State: Off
2. State: On

Properties:
- State: Boolean
- Label Left: Text
- Label Right: Text
```

### 6. Auto Layout 設置

#### 卡片 Auto Layout
```
Direction: Vertical
Spacing: 20px
Padding: 25px
```

#### 按鈕組 Auto Layout
```
Direction: Horizontal
Spacing: 15px
Padding: 0
```

#### 統計區域 Auto Layout
```
Direction: Horizontal
Spacing: 15px
Wrap: Yes (if available)
```

### 7. 原型設置 (Prototype)

#### 按鈕點擊
```
Trigger: On Click
Action: Change to [Hover State]
Animation: Ease Out
Duration: 300ms
```

#### 開關切換
```
Trigger: On Click
Action: Change to [Opposite State]
Animation: Ease In Out
Duration: 400ms
```

### 8. 匯出設置

```
Assets 匯出:
- Icon assets: SVG
- Images: PNG @2x
- Background: PNG or CSS Gradient code

Code Export:
- 使用 Figma CSS 匯出功能
- 複製顏色碼和間距值
```

---

## 使用圖示 (Icons/Emojis)

本設計使用 Unicode Emoji，無需額外圖示庫：

```
🐁 - 滑鼠 (主標題)
⚙️ - 設定 (控制面板)
📊 - 統計 (統計資訊)
📝 - 記錄 (活動日誌)
🖥️ - 電腦 (視覺化畫布)
▶️ - 播放 (開始按鈕)
⏹️ - 停止 (停止按鈕)
🔄 - 重新整理 (重置按鈕)
😺 - 貓咪 (程式自動移動)
🐱 - 貓臉 (畫布上的自動移動標記)
👆 - 手指 (使用者點擊)
🐁 - 老鼠 (位置變更)
👋 - 揮手 (停止訊息)
🚀 - 火箭 (開始訊息)
⚠️ - 警告 (Hot Corner 警告)
```

---

## 動畫規格

### 過渡時間 (Transition Duration)

```
快速: 150ms - 200ms
- 用於：按鈕狀態變化、顏色變化

標準: 300ms
- 用於：懸停效果、陰影變化

慢速: 400ms
- 用於：開關切換、佈局變化
```

### 緩動函數 (Easing Functions)

```
ease: 標準過渡
ease-in: 淡入效果
ease-out: 淡出效果
ease-in-out: 平滑過渡

用途:
- 按鈕: ease-out
- 開關: ease-in-out
- 懸停: ease
```

---

## 可訪問性 (Accessibility)

### WCAG 2.1 AA 標準

#### 顏色對比
```
文字與背景:
- 正文: 至少 4.5:1
- 大文字 (18pt+): 至少 3:1
- UI 組件: 至少 3:1

已驗證組合:
✓ #333333 on #ffffff (12.6:1)
✓ #667eea on #ffffff (4.5:1)
✓ #ffffff on #667eea (4.5:1)
✓ #495057 on #e9ecef (7.9:1)
```

#### 鍵盤導航
```
Tab 順序:
1. 時間滑桿
2. 小範圍開關
3. 持續執行開關
4. 開始按鈕
5. 停止按鈕
6. 重置按鈕
7. 畫布區域
```

#### 焦點狀態
```
所有互動元素應有明顯焦點指示:
- outline: 2px solid #667eea
- outline-offset: 2px
```

#### 螢幕閱讀器
```
重要元素需添加 ARIA 標籤:
- aria-label
- aria-describedby
- role 屬性
```

---

## 實作清單 (Implementation Checklist)

### Figma 設置
- [ ] 建立新專案 "Mouse Rover"
- [ ] 設定畫布尺寸 (1400px)
- [ ] 設定網格系統 (12欄, 8px基準)
- [ ] 建立色彩樣式庫 (20+ 顏色)
- [ ] 建立文字樣式庫 (8+ 樣式)
- [ ] 建立效果樣式 (陰影、模糊)

### 組件建立
- [ ] 按鈕組件 (3種類型 x 3種狀態)
- [ ] 卡片組件
- [ ] 統計卡片組件
- [ ] 滑桿組件
- [ ] 開關組件
- [ ] 資訊框組件
- [ ] 命令框組件
- [ ] 日誌條目組件

### 頁面組成
- [ ] Header 區域
- [ ] 控制面板卡片
- [ ] 統計資訊卡片
- [ ] 活動日誌卡片
- [ ] 視覺化畫布卡片
- [ ] 整體佈局組裝

### 互動原型
- [ ] 按鈕懸停效果
- [ ] 開關切換動畫
- [ ] 滑桿拖動效果
- [ ] 頁面滾動行為

### 響應式設計
- [ ] Desktop 版本 (1400px)
- [ ] Tablet 版本 (768px)
- [ ] Mobile 版本 (375px)

### 匯出與交付
- [ ] 匯出設計規格 (CSS)
- [ ] 匯出切圖資源
- [ ] 建立設計系統文檔
- [ ] 開發者交付包

---

## 技術備註

### CSS 變數建議

```css
:root {
  /* Colors */
  --primary: #667eea;
  --primary-dark: #764ba2;
  --success: #28a745;
  --info: #007bff;
  --danger: #dc3545;

  /* Grays */
  --gray-50: #f8f9fa;
  --gray-100: #e9ecef;
  --gray-500: #6c757d;
  --gray-900: #1e1e1e;

  /* Spacing */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 40px;

  /* Border Radius */
  --radius-sm: 5px;
  --radius-md: 10px;
  --radius-lg: 15px;
  --radius-xl: 20px;
  --radius-full: 50%;

  /* Shadows */
  --shadow-sm: 0 2px 4px rgba(0,0,0,0.1);
  --shadow-md: 0 4px 6px rgba(0,0,0,0.07);
  --shadow-lg: 0 20px 60px rgba(0,0,0,0.3);

  /* Transitions */
  --transition-fast: 150ms;
  --transition-base: 300ms;
  --transition-slow: 400ms;
}
```

---

## 設計資源

### 字體下載
- System Fonts (內建)
- Courier New (等寬字體)

### 顏色工具
- Coolors.co - 配色方案
- WebAIM Contrast Checker - 對比度檢查
- ColorBox by Lyft - 色彩系統生成

### Figma 插件推薦
- **Contrast** - 檢查顏色對比度
- **Autoflow** - 繪製流程圖
- **Content Reel** - 填充示例內容
- **Iconify** - 圖示庫（如需替換 emoji）
- **Component Inspector** - 組件檢查
- **Design Lint** - 設計規範檢查

---

## 更新記錄

| 版本 | 日期 | 更新內容 |
|------|------|----------|
| 1.0 | 2025-10-22 | 初始版本，完整設計規格 |

---

## 聯絡資訊

如有設計相關問題，請參考：
- 互動式演示: `demo.html`
- 原始碼: `mouse-rover.py`
- 專案 README: `README.md`

---

**設計規格文檔結束**

本文檔提供完整的視覺設計規範，適用於 Figma、Sketch、Adobe XD 等設計工具實作。
