<template>
    <v-app>
        <canvas id="stars"></canvas>
        <div class="bg-overlay"></div>
        <router-view></router-view>
    </v-app>
</template>

<script setup lang='ts'>
    import {onMounted} from "vue";
    import useNoteStore from "@/store/blog/storages/note.ts";
    import useDiaryStore from "@/store/blog/storages/diary.ts";
    import useSiteInformationStore from "@/store/blog/storages/site_info.ts";
    import useAboutMeStore from "@/store/blog/storages/about_me.ts";
    import axios_server from "./utils/axios_server.ts";
    import type {MyAbilityAndMySkill, MyTask, MyFavoriteLink} from "@/store/blog/types/about_me.ts";
    import dayjs from "dayjs";
    import type {SiteSocialLink} from "@/store/blog/types/site_info.ts";
    import type {NoteListItem} from "@/store/blog/types/note.ts";
    import type {DiaryListItem} from "@/store/blog/types/diary.ts";

    defineOptions({
        name: 'App',
        inheritAttrs: false
    })

    let noteStore = useNoteStore()
    let diaryStore = useDiaryStore()
    let siteInformationStore = useSiteInformationStore()
    let aboutMeStore = useAboutMeStore()

    onMounted(() => {
        // 从后端获取所有的NoteList
        axios_server.get('/api/note/list').then(
            (response) => {
                noteStore.noteList = response.data
                noteStore.noteList.forEach((value:NoteListItem) => {
                    value.createdTime = dayjs(value.createdTime).format('YYYY-MM-DD')
                    value.updatedTime = dayjs(value.updatedTime).format('YYYY-MM-DD')
                })
            }
        )

        // 从后端获取所有的DiaryList
        axios_server.get('/api/diary/list').then(
            (response) => {
                diaryStore.diaryList = response.data
                diaryStore.diaryList.forEach((value:DiaryListItem) => {
                    value.createdTime = dayjs(value.createdTime).format('YYYY-MM-DD')
                    value.updatedTime = dayjs(value.updatedTime).format('YYYY-MM-DD')

                    const randomIndex = Math.floor(Math.random() * diaryStore.timelineColors.length)
                    value.timelineColor = {
                        pointColor: diaryStore.timelineColors[randomIndex].pointColor,
                        textColor: diaryStore.timelineColors[randomIndex].textColor
                    }
                })
            }
        )

        // 从后端获取博客网站信息
        axios_server.get('/api/site_config/site_info').then(
            (response) => {
                Object.assign(siteInformationStore.siteInformation, response.data)
                siteInformationStore.siteInformation.createdTime = dayjs(siteInformationStore.siteInformation.createdTime).format('YYYY-MM-DD')
                siteInformationStore.siteInformation.updatedTime = dayjs(siteInformationStore.siteInformation.updatedTime).format('YYYY-MM-DD')
            }
        )

        // 从后端获取about me的信息：my_detail、my_ability、my_detail、my_task、my_favorite_link
        axios_server.get('/api/about_me/my_detail').then(
            (response) => {
                // 获取my_detail
                Object.assign(aboutMeStore.myDetail, response.data)
            }
        )
        axios_server.get('/api/about_me/my_ability').then(
            (response) => {
                // 获取my_ability
                response.data.forEach((value: MyAbilityAndMySkill) => {
                    aboutMeStore.myAbility.push(value)
                })
            }
        )
        axios_server.get('/api/about_me/my_skill').then(
            (response) => {
                // 获取my_skill
                response.data.forEach((value: MyAbilityAndMySkill) => {
                    aboutMeStore.mySkill.push(value)
                })
            }
        )
        axios_server.get('/api/about_me/my_task').then(
            (response) => {
                // 获取my_task
                response.data.forEach((value: MyTask) => {
                    aboutMeStore.myTask.push(value)
                    aboutMeStore.myTask.forEach((value: MyTask) => {
                        value.createdTime = dayjs(value.createdTime).format('YYYY-MM-DD')
                    })
                })
            }
        )
        axios_server.get('/api/about_me/my_favorite_link').then(
            (response) => {
                // 获取my_favorite_link
                response.data.forEach((value: MyFavoriteLink) => {
                    aboutMeStore.myFavoriteLink.push(value)
                })
            }
        )

        // 从后端获取social_info_link
        axios_server.get('/api/site_config/site_social_info').then(
            (response) => {
                response.data.forEach((value: SiteSocialLink) => {
                    siteInformationStore.siteSocialLinkList.push(value)
                })
            }
        )

        const canvas = document.getElementById("stars") as HTMLCanvasElement;
        const ctx = canvas.getContext("2d")!;
        const stars: { x: number, y: number, r: number, vx: number, vy: number }[] = [];
        const STAR_COUNT = 20;

        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        for (let i = 0; i < STAR_COUNT; i++) {
            stars.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                r: Math.random() * 2 + 1,
                vx: (Math.random() - 0.5) * 0.5,
                vy: (Math.random() - 0.5) * 0.5
            });
        }

        function draw() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            stars.forEach(s => {
                ctx.beginPath();
                ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
                ctx.fillStyle = "white";
                ctx.shadowColor = "white";
                ctx.shadowBlur = s.r * 5;
                ctx.fill();
                s.x += s.vx;
                s.y += s.vy;
                if (s.x < 0 || s.x > canvas.width) s.vx *= -1;
                if (s.y < 0 || s.y > canvas.height) s.vy *= -1;
            });
            requestAnimationFrame(draw)
        }

        draw()
    })
</script>

<style lang="scss">
    #stars {
        width: 100vw;
        height: 100vh;
        position: fixed;
        inset: 0;
        z-index: 0;
        pointer-events: none;
        background: black;
        opacity: 1;
    }

    .bg-overlay {
        width: 100vw;
        height: 100vh;
        position: fixed;
        inset: 0;
        z-index: 0;
        background: radial-gradient(ellipse at center,
            rgba(17, 60, 70, 0.1) 0%,
            rgba(17, 60, 70, 0.15) 25%,
            rgba(17, 60, 70, 0.2) 50%,
            rgba(17, 60, 70, 0.25) 75%,
            rgba(17, 60, 70, 0.3) 100%);
        pointer-events: none;
    }
</style>