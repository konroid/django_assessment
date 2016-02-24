from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models import Post,Comment
from serializers import SerializePost,SerializeComment


@api_view(['GET', 'POST'])
def post_list(request):
        #
        # List all posts, or create a new post
        #
    if request.method == 'GET':
        #r = requests.get('http://jsonplaceholder.typicode.com/posts')
        #posts = r.json()
        posts = Post.objects.all()
        serializer = SerializePost(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SerializePost(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT'])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SerializePost(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SerializePost(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def comment_list(request):
    #
    # List all comments for a post, or create a new comment for a post
    #
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = SerializeComment(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SerializeComment(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def comment_detail(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SerializeComment(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SerializeComment(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def comments_post(request, pk):
    try:
        comment = Comment.objects.get(postId=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
#        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SerializeComment(comment)
        return Response(serializer.data)

    else:
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
