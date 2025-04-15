import type {Tag} from "@/store//blog/types/tag.ts";

interface TimelineColor {
    pointColor: string,
    textColor: string
}

export interface DiaryListItem {
    "diaryListId": number,
    "title": string,
    "brief": string,
    "coverImg": string,
    'tags': Tag[],
    "createdTime": string,
    "updatedTime": string,
    "viewCount": number,
    "readingTime": number,
    "wordCount": number
    "timelineColor": TimelineColor,
}

export interface DiaryContentItem {
    "diaryListId": number,
    "title": string,
    "brief": string,
    "coverImg": string,
    'tags': Tag[],
    "createdTime": string,
    "updatedTime": string,
    "viewCount": number,
    "readingTime": number,
    "wordCount": number
    "markdownContent": string,
    "imageUrls": string[],
    "renderedMarkdown": string
}