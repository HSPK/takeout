import jieba
import jieba.posseg as pseg
import codecs

def all_chinese(str):
   for ch in str:
      if not ('\u4e00' <= ch <= '\u9fff'):
         return False
   return True


PP = ('好', '多', '便宜', '')
jieba.enable_paddle()
with codecs.open("comment.csv", "r", encoding='utf8') as comments:
    words = jieba.cut(comments.readline(), use_paddle=True) # paddle模式分词
    print('/'.join([word for word in words if all_chinese(word)]))