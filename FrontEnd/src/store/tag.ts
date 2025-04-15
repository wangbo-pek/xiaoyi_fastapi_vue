import {defineStore} from "pinia";
import type {TagWithCount} from "@/store/types/tag.ts";

const useTagStore = defineStore('tags', {
    state: () => {
        return {
            tagList:[] as TagWithCount[]
        }
    }
})

export default useTagStore