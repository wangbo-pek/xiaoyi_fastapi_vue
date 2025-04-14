import type {Tag} from "@/store/types/tag.ts"
import type {Category} from "@/store/types/category.ts"


export interface NoteListItem {
    "noteListId": number,
    "title": string,
    "brief": string,
    "coverImg": string,
    'slug': string,
    'keyword': string,
    'description': string,
    'category': Category,
    'tags': Tag[],
    "isPinned": boolean,
    "isRecommended": boolean,
    "createdTime": string,
    "updatedTime": string,
    "viewCount": number,
    "likeCount": number,
    "dislikeCount": number,
    "readingTime": number,
    "wordCount": number
}

export interface NoteContentItem {
    "noteListId": number,
    "title": string,
    "brief": string,
    "coverImg": string,
    "isShow": boolean,
    "isPinned": boolean,
    "isRecommended": boolean,
    "viewedCount": number,
    "likedCount": number,
    "disgustedCount": number,
    "encouragedCount": number,
    "createdTime": string,
    "modifiedTime": string,
    "tagsName": string[],
    "category": string,
    "markdownContent": string,
    "htmlContent": string,
    "imageUrls": string[],
    "renderedMarkdown": string,
    "tableOfContent": string
}
