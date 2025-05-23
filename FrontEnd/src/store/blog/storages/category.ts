import {defineStore} from "pinia";
import type {CategoryWithCount} from "@/store/blog/types/category.ts";

const useCategoryStore = defineStore('categories', {
    state: () => {
        return {
            categoryList:[] as CategoryWithCount[]
        }
    }
})

export default useCategoryStore