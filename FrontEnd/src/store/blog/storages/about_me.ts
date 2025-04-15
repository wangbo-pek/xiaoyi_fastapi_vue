import {defineStore} from "pinia";
import type {MyDetail, MyAbilityAndMySkill, MyFavoriteLink, MyTask} from "@/store/blog/types/about_me.ts";

const useAboutMeStore = defineStore('aboutMe', {
    state: () => {
        return {
            myDetail: {} as MyDetail,
            myAbility: [] as MyAbilityAndMySkill[],
            mySkill: [] as MyAbilityAndMySkill[],
            myTask: [] as MyTask[],
            myFavoriteLink: [] as MyFavoriteLink[],
        }
    }
})
export default useAboutMeStore