import {defineStore} from "pinia";
import type {NoteListItem, NoteContentItem} from "@/store/types/note.ts";

const useNoteStore = defineStore('note', {
    state: () => {
        return {
            noteList: [] as NoteListItem[],
            currentNote: {
                noteListId: 0,
                title: '',
                brief: '',
                coverImg: '',
                slug: '',
                keyword: '',
                description: '',
                category: {name: '', description: ''},
                tags: [],
                isPinned: false,
                isRecommended: false,
                createdTime: '',
                updatedTime: '',
                viewCount: 0,
                likeCount: 0,
                dislikeCount: 0,
                readingTime: 0,
                wordCount: 0,
                markdownContent: '',
                imageUrls: [],
                renderedMarkdown: '',
                tableOfContent: ''
            } as NoteContentItem,
            recommendedNoteList: [] as NoteListItem[],
            latestNoteList: [] as NoteListItem[]
        }
    }
})
export default useNoteStore