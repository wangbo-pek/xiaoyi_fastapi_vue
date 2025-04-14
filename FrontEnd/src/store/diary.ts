import {defineStore} from "pinia";
import type {DiaryListItem} from "@/store/types/diary.ts";

const useDiaryStore = defineStore('diary', {
    state: () => {
        return {
            diaryList: [] as DiaryListItem[],
            currentDiary: {
                "diaryListId": 0,
                "title": '',
                "brief": '',
                "coverImg": '',
                "isShow": false,
                "viewedCount": 0,
                "createdTime": '',
                "modifiedTime": '',
                "markdownContent": '',
                "htmlContent": '',
                "imageUrls": [],
                "renderedMarkdown": ''
            },
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