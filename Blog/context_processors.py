#-*- coding: utf-8 -*-
#***********************************************
#
#      Filename: context_processors.py
#
#        Author: Benson - zjxucb@gmail.com
#   Description: ---
#        Create: 2018-01-19 09:50:48
# Last Modified: 2018-01-19 09:50:49
#***********************************************

__author__ = 'Benson'

from blog.models import Category, Article, Tag, Comment


def sidebar(request):
    category_list = Category.objects.all()
    # 所有类型

    article_rank = Article.objects.all().order_by('-view')[0:6]
    # 文章排行

    tag_list = Tag.objects.all()
    # 标签

    comment = Comment.objects.all().order_by('-create_time')[0:6]
    # 评论

    return {
        'category_list': category_list,
        'article_rank': article_rank,
        'tag_list': tag_list,
        'comment_list': comment

    }


if __name__ == '__main__':
    pass
