import datetime

from django.http import Http404
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from rest_framework import viewsets, permissions, parsers, status
from rest_framework.exceptions import NotFound as NotFoundError
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView