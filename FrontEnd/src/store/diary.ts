import {defineStore} from "pinia";
import type {DiaryContentItem, DiaryListItem} from "@/store/types/diary.ts";

const useDiaryStore = defineStore('diary', {
    state: () => {
        return {
            diaryList: [] as DiaryListItem[],
            currentDiary: {
                diaryListId: 0,
                title: '',
                brief: '',
                coverImg: '',
                tags: [],
                createdTime: '',
                updatedTime: '',
                viewCount: 0,
                readingTime: 0,
                wordCount: 0,
                markdownContent: '',
                imageUrls: [],
                renderedMarkdown: '',
                tableOfContent: ''
            } as DiaryContentItem,
            timelineColors: [
                {pointColor: 'rgba(240,250,90,0.35)', textColor: 'rgba(255,255,255,0.65)'},
                {pointColor: 'rgba(170,240,90,0.35)', textColor: 'rgba(255,255,255,0.65)'},
                {pointColor: 'rgba(50,180,100,0.35)', textColor: 'rgba(255,255,255,0.65)'},
                {pointColor: 'rgba(80,230,200,0.35)', textColor: 'rgba(255,255,255,0.65)'},
                {pointColor: 'rgba(80,150,220,0.35)', textColor: 'rgba(255,255,255,0.65)'}
            ]
        }
    }
})

export default useDiaryStore