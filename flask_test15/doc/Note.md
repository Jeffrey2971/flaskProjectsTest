 # Flask-RESTful

- 框架用来简化快速开发
- 帮助开发者快速实现REST接口



# 使用 

- 先配置
  - 安装 pip install flask-restful
  - 初始化
    - 使用APP对象对API对象进行初始化
    - 转换views
      - 可以是一个类
      - 也可是一个包
        - 使用包可拥有子文件
        - 创建一个views包
        - 在__init__中进行初始化
        - 创建子文件，在文件中创建自己的Resource,并写逻辑
        - 在API上注册resource
- 使用
  - API添加资源时，需要制定自己所需要的方法
  - 实现对应方法请求方式的名字
- 返回
  - 直接可使用字典，列表也支持
    - 使用对象需要手动进行初始化或进行格式定制
    - marshal_with装饰器



### 输出字段格式化

- 首先应该明确自己想要输出什么格式
  - 一般在需求确认之后，确定完数据库之后
  - 就需要和前端或移动端确定返回字段
    - 后端直接决定
    - 有时也需和前段沟通，传递特殊字段
- 把想要的格式定义好
  - 使用fields中的字段进行
  - 基本字段
    - String
    - Integer
    - Url
    - Date
      - 括号中可添加约束
      - attribute 映射属性名
      - default 默认值
      - url absolute 绝对路径
  - 级联字段
    - Nested  对应的是另外一个格式化字典
    - List  对应的是一个列表



### 输入数据的参数制定

- 正对于输入的数据进行预判断
- 使用reqparse.RequestParser()
  - 在对象上添加参数
  - 可以指定参数名
  - 可以指定参数类型
  - 可以制定参数出现错误时的提示
- 参数定制
  - 确认需要那些参数
    - 根据实际需求
  - 确认参数是否必须
    - add_argument 上添加required=True 必须的
  - 确认参数来源
    - location
      - args  自动
      - form  自动
      - headers
      - cookies
      - files



#### API 接口开发

- 确定数据，创建模型
- 创建接口资源
  - 创建Resource子类，实现数据曾删改查
  - 单个数据操作
    - 单数，接收ID
  - 批量数据操作拆分开
    - 复数，不接受ID（路径参数）
  - 输入输出格式化
    - 输入输出格式化
      - 通过reqparse.RequestParser进行参数的限定
        - 允许哪些参数
        - 从哪些位置获取参数
        - 获取的参数类型是什么
    - 输出格式化
      - 通过marshal_with装饰器来实现数据格式化
        - 可以对字典，对象，model进行格式化
        - 级联数据也能使用
      - marshal和marshal_with功能基本一致
      - 就是啷个参数
        - 第一个参数是原数据
        - 第二个参数是格式化后的数据