from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from langchain_groq import ChatGroq
from markdown import markdown

from chatbot.models import Chat
from decouple import config


def get_chat_history(chats):
    chat_history = []
    for chat in chats:
        chat_history.append(
            ('human', chat.message)
        )
        chat_history.append(
            ('ai', chat.response)
        )
    return chat_history


def ask_ai(context, message):
    try:
        model = ChatGroq(
            model='llama-3.2-90b-vision-preview',
            api_key=settings.GROQ_API_KEY,
        )
    except Exception as error:
        raise error
    messages = [
        (
            'system',
            'Você é um assistente responsável por tirar dúvidas sobre programação Python.'
            'Sempre traga o código em python bem detalhado e explicado'
            'Responda em formato markdown.',
        ),
    ]
    messages.extend(context)
    messages.append(
        (
            'human',
            message,
        )
    )
    print(messages)
    response = model.invoke(messages)
    return markdown(response.content, output_format='html')


def chatbot(request):
    template_name = 'chatbot/chatbot.html'
    chats = Chat.objects.all()

    if request.method == 'POST':
        context = get_chat_history(
            chats=chats,
        )
        message = request.POST.get('message')
        response = ask_ai(
            context=context,
            message=message
        )

        chat = Chat(
            message=message,
            response=response,
        )
        chat.save()

        context = {
            'message': message,
            'response': response
        }
        return JsonResponse(context)
    context = {
        'chats': chats
    }
    return render(request, template_name, context)
