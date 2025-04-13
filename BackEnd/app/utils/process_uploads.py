"""
    path: xiaoyi/BackEnd/utils/process_uploads.py
    description: 处理本地uploads文件夹内的待处理的markdown文件、插入、封面
"""
import re
from pathlib import Path
from app.utils.oss_upload import upload_to_oss
from app.crud.diary import create_diary_and_list
from app.crud.note import create_note_and_list
from app.schema.note import NoteCreate, NoteListCreate
from app.schema.diary import DiaryCreate, DiaryListCreate
from app.core.database import SessionLocal


# 用于提取markdown中的纯文本摘要
def extract_text(md_text: str, max_length: int = 100) -> str:
    cleaned = re.sub(r"!\[.*?]\(.*?\)", "", md_text)
    cleaned = re.sub(r"^#{1,6}\s*", "", cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r"\*\*.*?\*\*", "", cleaned)
    cleaned = re.sub(r"\*.*?\*|_.*?_", "", cleaned)
    cleaned = re.sub(r"\[.*?]\(.*?\)", "", cleaned)
    cleaned = re.sub(r"(_.*?_)", "", cleaned)
    cleaned = re.sub(r"~~.*?~~", "", cleaned)
    cleaned = re.sub(r"^>\s*", "", cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r"`.*?`", "", cleaned)
    cleaned = re.sub(r"```[\s\S]*?```", "", cleaned)
    cleaned = re.sub(r"^\d+\.\s*", "", cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r"^[-*+]\s*", "", cleaned, flags=re.MULTILINE)
    cleaned = cleaned.strip()
    return cleaned[:max_length]


def process_uploads():
    upload_path = Path("/Users/wangbo/Documents/uploads")
    if not upload_path.exists():
        print(f"❌错误❌ 上传目录不存在：{upload_path}")
        return

    for folder in upload_path.iterdir():
        folder_name = folder.name.strip()
        if not folder.is_dir() or folder_name.endswith('_uploaded') or folder_name.endswith('_preparation'):
            continue

        print(f'\n✨开始处理✨{folder_name}')

        is_note = folder_name.startswith('note')
        is_diary = folder_name.startswith('diary')
        if not is_note and not is_diary:
            print(f'跳过{folder_name}，不是note或diary')

        # 获取路径
        md_file = None
        for f in folder.iterdir():
            if f.suffix == '.md':
                md_file = f
                break

        cover_path = folder / 'cover.jpg'
        pictures_path = folder / 'pictures'

        if not md_file or not cover_path.exists():
            print(f'⚠️缺少⚠️ .md 或 cover.jpg，跳过：{folder_name}')
            continue

        # 上传封面图
        cover_url = upload_to_oss(cover_path, f'images/{folder_name}/cover.jpg')

        # 上传插图并建立映射
        image_mapping = {}
        if pictures_path.exists():
            for image_file in pictures_path.iterdir():
                if image_file.suffix.lower() not in {'.jpg', '.jpeg', '.png', '.gif', '.webp'}:
                    continue
                oss_key = f'images/{folder_name}/pictures/{image_file.name}'
                oss_url = upload_to_oss(image_file, oss_key)
                image_mapping[image_file.name] = oss_url
        image_urls = list(image_mapping.values())

        # 读取markdown内容并替换插图路径为oss_url
        with md_file.open('r', encoding='utf-8') as f:
            md_content = f.read()

        for image_name, oss_url in image_mapping.items():
            md_content = md_content.replace(f'pictures/{image_name}', oss_url)

        title = md_file.stem
        lines = md_content.strip().splitlines()

        brief = ''
        category = ''
        tags = []

        # 提取摘要（第一个引用段落）
        for line in lines:
            if line.strip().startswith('>'):
                brief = extract_text(line)
                break

        # 提取分类和标签（最后一行）
        if lines:
            last_line = lines[-1]
            if is_note and last_line.startswith('@'):
                parts = last_line.split()
                if parts:
                    category = parts[0][1:].strip()
                    tags = [p[1:] for p in parts[1:] if p.startswith('#')]
                lines = lines[:-1]
            elif is_diary and last_line.strip().startswith('#'):
                tags = [t[1:] for t in last_line.strip().split() if t.startswith('#')]
                lines = lines[:-1]

        # 去除结构行后的 markdown 内容
        content = '\n'.join(lines)

        db = SessionLocal()
        # 创建数据
        try:
            if is_note:
                create_note_and_list(
                    db=db,
                    note_data=NoteCreate(
                        title=title,
                        content=content,
                        image_url=image_urls
                    ),
                    note_list_data=NoteListCreate(
                        title=title,
                        brief=brief,
                        cover_img=cover_url,
                        category=category,
                        tags=tags
                    )
                )
                print(f'✅ 成功保存笔记：{title}')
                # 重命名文件夹
                new_folder = folder.with_name(folder_name + '_uploaded')
                folder.rename(new_folder)
                print(f'✅处理完毕并已重新命名：{new_folder.name}')
            elif is_diary:
                create_diary_and_list(
                    db=db,
                    diary_data=DiaryCreate(
                        title=title,
                        content=content,
                        image_url=image_urls
                    ),
                    diary_list_data=DiaryListCreate(
                        title=title,
                        brief=brief,
                        cover_img=cover_url,
                        tags=tags
                    )
                )
                print(f'✅ 成功保存笔记：{title}')
                # 重命名文件夹
                new_folder = folder.with_name(folder_name + '_uploaded')
                folder.rename(new_folder)
                print(f'✅处理完毕并已重新命名：{new_folder.name}')
        except Exception as e:
            print(f'❌ 处理失败：{folder_name}，错误：{e}')

if __name__ == '__main__':
    process_uploads()

