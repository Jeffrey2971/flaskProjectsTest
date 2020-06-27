### 前后端分离
- 前段不写了，交给前端的工程师
    - html,css,js
    - 没有语法和模板
- 主要实现后端
    - 数据，增删查改
- 前后单交互
    - JSON 数据交换格式
    - 前端使用Ajax和后端进行交互
### REST
- 

### 前端
- JS中获取请求参数
- 可以导入库来实现
- 手动实现
    - http://127.0.0.1:5000/static/html/StudentDetail.html?id=4&name=Jeffrey
    - 根据第一个 ? 进行剪切、分割 获取 ? 后的部分
    - id=4&name=Jeffrey
    - 再次根据 & 分割
    - id = 4
    - 根据 = 切割
    - 前面的是key,后面的是value
- JS内的循环添加点击时为什么不能用i
    - 作用域问题