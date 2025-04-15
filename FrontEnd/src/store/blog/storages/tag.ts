import {defineStore} from "pinia";
import type {TagWithCount} from "@/store/blog/types/tag.ts";

const useTagStore = defineStore('tags', {
    state: () => {
        return {
            tagList:[] as TagWithCount[]
        }
    }
})

export default useTagStore