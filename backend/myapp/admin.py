# backend/myapp/admin.py
from django.contrib import admin
from .models import Author, Book, Chapter
from django.utils.html import format_html
from .models import Photo
# backend/myapp/admin.py
admin.site.site_header = "My Company Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "관리자 대시보드"
# --- Inline 사용: Book 내에서 Chapter 관리 ---
class ChapterInline(admin.StackedInline):
    model = Chapter
    fields = ('title', 'description', 'content')  # 표시 순서/칼럼 지정
    extra = 1  # 추가 빈칸 수

# --- Book 관리 ---
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'status')
    list_filter = ('status', 'published_date', 'author')
    search_fields = ('title', 'author__name')
    ordering = ('-published_date',)
    inlines = [ChapterInline]

    # 커스텀 액션: 선택한 책 발행
    actions = ['mark_as_published']

    def mark_as_published(self, request, queryset):
        updated = queryset.update(status='published')
        self.message_user(request, f"{updated}개의 책을 발행 상태로 변경했습니다.")
    mark_as_published.short_description = "선택한 책을 발행 상태로 변경"

# --- Author 관리 ---
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name',)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'image_tag')
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 200px;"/>', obj.image.url)
        return "-"
    image_tag.short_description = '미리보기'