from django.shortcuts import render
from django.http import HttpResponse

def mission_view(request):
    mission_essay = "The University is a private non-stock, non-profit, non sectarian educational foundation with a three-fold function - instruction, research and community service offering responsive and alternative programs supportive of national development goals and standards of global excellence."
    return HttpResponse(mission_essay)

def vision_view(request):
    vision_essay = "In 2030, the Manuel S. Enverga University Foundation is a globally competitive university with high concentration of talent, excellent teaching environment, rigorous program quality, sufficient resources, and a culture of collaboration."
    return HttpResponse(vision_essay)

def objectives_view(request):
    objectives_essay = "The University Libraries recognize their roles as instruments of teaching, research and extension in the academe. The organization of all materials and resources, the facilities provided, selection, training, and management of the staff, are all geared toward the fulfillment of these roles. The general objective of the University Libraries System is to gather, organize and service a collection of library materials print and non-print, book and non-book in support of the University’s educational programs."
    return HttpResponse(objectives_essay)
