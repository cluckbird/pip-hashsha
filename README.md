# Python 快捷運算哈希 256 / 512 / 1


鍵入以下命令安裝這個庫：

```
pip install fasthash
```

## 該模塊較為簡潔，使用方式如下

```python
sha1("示例字符串")   #返回哈希1
sha256("示例字符串") #返回哈希256
sha512("示例字符串") #返回哈希512
```

## 使用例

```python
import fasthash

hash256_b = fasthash.sha256("測試內容")
print(hash256_b)
```
