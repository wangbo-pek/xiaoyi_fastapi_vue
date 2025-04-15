<template>
    <div class="header">
        <Header></Header>
    </div>
    <div class="about-container">
        <div class="my-avatar">
            <v-img class="my-avatar-icon"
                   :src="aboutMeStore.myDetail.avatar"></v-img>
        </div>
        <div class="my-name">
            <span class="my-name-text">{{ aboutMeStore.myDetail.nickname }}</span>
        </div>

        <div class="my-formal-intro">
            <div class="my-formal-intro-text">
                {{ aboutMeStore.myDetail.fullIntro }}
            </div>
        </div>
        <div class="touch-me">
            <v-img class="wechat-icon"
                   :src="`https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/wechat.svg`"
                   @click="showWechatDialog = true">
            </v-img>
            <v-img class="mail-icon"
                   :src="`https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/gmail.svg`"
                   @click="touchMe('mailMe')">
            </v-img>
            <v-img class="rss-icon"
                   :src="`https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/rss.svg`"
                   @click="touchMe('rssMe')">
            </v-img>

        </div>

        <div class="my-ability-title">
            ——&nbsp;&nbsp;&nbsp;我的能力&nbsp;&nbsp;&nbsp;——
        </div>
        <div class="my-ability">
            <div class="my-ability-radar">
                <MyAbilitiesRadar></MyAbilitiesRadar>
            </div>
            <div class="my-skills-progress">
                <template v-for="(item) in aboutMeStore.mySkill" :key="item.name">
                    <MySkillProgress :name="item.title" :level="item.degree"></MySkillProgress>
                </template>
            </div>
        </div>

        <div class="my-current-works-title">
            ——&nbsp;&nbsp;&nbsp;我的任务&nbsp;&nbsp;&nbsp;——
        </div>
        <div class="my-current-works">
            <div class="my-current-works-item" v-for="item in aboutMeStore.myTask" :key="item.title">
                <div class="my-current-works-content">
                    <div class="my-current-works-title-status">
                        <span class="my-current-works-titles">{{ item.title }}</span>
                        <span class="my-current-works-status" :class="item.status">{{ item.status }}</span>
                    </div>
                    <div class="my-current-works-description">{{ item.description }}</div>
                    <v-progress-linear
                        :model-value="item.progress"
                        height="8"
                        color="rgb(242, 204, 15)"
                        class="current-progress"
                        rounded
                        striped
                        background-opacity="0.2"
                    ></v-progress-linear>
                </div>
            </div>
        </div>

        <div class="my-favorite-link-title">
            ——&nbsp;&nbsp;&nbsp;我的收藏&nbsp;&nbsp;&nbsp;——
        </div>
        <div class="my-favorite-link">
            <template v-for="item in aboutMeStore.myFavoriteLink" :key="item.title">
                <div class="links-container">
                    <v-img class="link-icon"
                           :src="item.faviconUrl"></v-img>
                    <a :href="item.url" class="link-to-out-of-blog" target="_blank"><span
                        class="link-title">{{ item.title }}</span></a>
                    <v-icon v-if="item.isOutOfWall" class="need-a-ladder" size="20">mdi-ladder</v-icon>
                </div>
            </template>
        </div>

        <div class="my-all-cover-title">
            ——&nbsp;&nbsp;&nbsp;我的封面&nbsp;&nbsp;&nbsp;——
        </div>
        <div class="my-all-cover">
            <v-carousel
                show-arrows="hover"
                hide-delimiters
                cycle
                interval="10000"
            >
                <v-carousel-item
                    v-for="(item, index) in allCover"
                    :key="index"
                    :src="item"
                >
                </v-carousel-item>
            </v-carousel>
        </div>

        <div class="placeholder"></div>

        <Footer></Footer>
    </div>

    <!-- 我的微信二维码 -->
    <v-dialog v-model="showWechatDialog" width="500">
        <v-card class="qr-card" color="#1e1e1e">
            <v-card-title class="text-center text-white">微信扫一扫</v-card-title>
            <v-card-text class="text-center">
                <v-img
                    :src="aboutMeStore.myDetail.wechatQR"
                    aspect-ratio="1"
                    contain
                />
            </v-card-text>
            <v-card-actions class="justify-center">
                <v-btn color="rgb(242, 204, 15)" @click="showWechatDialog = false">关闭</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>

</template>

<script setup lang='ts'>
    import {onMounted, onUnmounted, ref, watch} from "vue";
    import useAboutMeStore from "@/store/blog/storages/about_me.ts";
    import useAppearanceStore from "@/store/blog/storages/appearance.ts";
    import useNoteStore from "@/store/blog/storages/note.ts";
    import useDiaryStore from "@/store/blog/storages/diary.ts";
    import Header from "@/components/blog/header/Header.vue";
    import Footer from "@/components/blog/footer/Footer.vue";
    import MyAbilitiesRadar from "@/components/blog/MyAbilitiesRadar.vue"
    import MySkillProgress from "@/components/blog/MySkillProgress.vue"
    import type {NoteListItem} from "@/store/blog/types/note.ts";
    import type {DiaryListItem} from "@/store/blog/types/diary.ts";

    defineOptions({
        name: 'About',
        inheritAttrs: false
    })

    const aboutMeStore = useAboutMeStore()
    let appearanceStore = useAppearanceStore()
    const noteStore = useNoteStore()
    const diaryStore = useDiaryStore()
    let allCover: string[] = []
    const showWechatDialog = ref(false)  // 控制微信二维码 dialog

    onMounted(() => {
        appearanceStore.isShowHomeCover = false
        appearanceStore.isScrollOverViewport = true

        setTimeout(() => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            })
        }, 10)
    })

    onUnmounted(() => {
        appearanceStore.isShowHomeCover = true
    })

    watch(() => [noteStore.noteList, diaryStore.diaryList], ([newNotes, newDiaries]) => {
            allCover.length = 0
            newNotes.forEach((value:NoteListItem|DiaryListItem) => allCover.push(value.coverImg))
            newDiaries.forEach((value:NoteListItem|DiaryListItem) => allCover.push(value.coverImg))
        }, {immediate: true, deep: true}
    )

    const touchMe = (name: string) => {
        const urlMap: Record<string, string> = {
            mailMe: 'mailto:wangbo.pek@gmail.com',
            rssMe: ''
        }
        const url = urlMap[name]
        if (url) {
            window.open(url, '_blank')
        }
    }

</script>

<style scoped lang='scss'>
    .header {
        padding: 0;
        margin: 0;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 8vh;
        z-index: 1000;
    }

    .about-container {
        position: relative;
        top: 10rem;

        .my-avatar {
            display: flex;
            justify-content: center;

            .my-avatar-icon {
                max-width: 12rem;
            }
        }

        .my-name {
            margin: 20px 0 20px 0;
            display: flex;
            justify-content: center;

            .my-name-text {
                color: white;
                font-size: 2rem;
                font-weight: 200;
            }
        }

        .my-formal-intro {
            display: flex;
            justify-content: center;
            margin: 10px 0 30px 0;

            .my-formal-intro-text {
                color: white;
                max-width: 50rem;
                font-size: 1rem;
                font-weight: 700;
                text-align: left;
                line-height: 30px;
            }
        }

        .touch-me {
            position: relative;
            width: 100%;
            display: flex;
            justify-content: center;

            .wechat-icon {
                margin: 0 20px 0 20px;
                max-width: 2rem;
                cursor: pointer;
            }

            .mail-icon {
                margin: 0 20px 0 20px;
                max-width: 2rem;
                cursor: pointer;
            }

            .rss-icon {
                margin: 0 20px 0 20px;
                max-width: 2rem;
                cursor: pointer;
            }
        }

        .my-ability-title {
            margin: 100px 0 30px 0;
            text-align: center;
            color: white;
            font-size: 1.75rem;
        }

        .my-ability {
            display: flex;
            justify-content: center;
            margin: 20px auto;

            .my-ability-radar {
                width: 40%;
            }

            .my-skills-progress {
                width: 40%;
                padding-top: 65px;
                padding-left: 150px;
            }

        }

        .my-current-works-title {
            text-align: center;
            color: white;
            font-size: 1.75rem;
            margin: 50px 0 30px 0;
        }

        .my-current-works {
            max-width: 750px;
            margin: 2rem auto;
            display: flex;
            flex-direction: column;
            gap: 2.5rem;

            .my-current-works-item {
                display: flex;
                background-color: rgba(0, 35, 35, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 16px;
                padding: 1.2rem 1.5rem;
                transition: transform 0.3s ease;

                &:hover {
                    transform: translateY(-4px);
                }

                .my-current-works-content {
                    flex: 1;

                    .my-current-works-title-status {
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                        margin-bottom: 0.5rem;

                        .my-current-works-titles {
                            font-size: 1.1rem;
                            font-weight: 700;
                            color: white;
                        }

                        .my-current-works-status {
                            font-size: 0.85rem;
                            padding: 4px 8px;
                            border-radius: 8px;
                            color: #fff;
                            font-weight: 600;
                        }

                        .未开始 {
                            background-color: #777;
                        }

                        .准备中 {
                            background-color: #ffa500;
                        }

                        .进行中 {
                            background-color: #2196f3;
                        }

                        .已完成 {
                            background-color: #4caf50;
                        }
                    }

                    .my-current-works-description {
                        font-size: 0.95rem;
                        color: #ddd;
                        line-height: 1.5;
                    }

                    .current-progress {
                        margin-top: 1rem;
                        width: 100%;
                    }
                }
            }
        }

        .my-favorite-link-title {
            margin: 100px 0 30px 0;
            text-align: center;
            color: white;
            font-size: 1.75rem;
        }

        .my-favorite-link-title {
            margin: 100px 0 30px 0;
            text-align: center;
            color: white;
            font-size: 1.75rem;
        }

        .my-favorite-link {
            width: 50%;
            margin: 0 auto;

            .links-container {
                display: flex;
                justify-content: flex-start;
                align-items: center;
                padding-bottom: 5px;
                margin-bottom: 20px;
                border-bottom: 1px solid rgba(255, 255, 255, 0.25);

                .link-icon {
                    max-width: 1rem;
                    margin-right: 10px;
                }

                .link-title {
                    background-image: linear-gradient(90deg, #e3ff07, #ffd21a, #fd9600, #ff8302);
                    background-clip: text;
                    color: transparent;
                    margin-right: 10px;
                }

                .need-a-ladder {
                    color: red;
                }
            }
        }

        .my-all-cover-title {
            margin: 100px 0 30px 0;
            text-align: center;
            color: white;
            font-size: 1.75rem;
        }

        .my-all-cover {
            width: 55%;
            margin: 0 auto;
        }

        .placeholder {
            margin-bottom: 75px;
        }
    }

    :deep(.v-slide-group__prev),
    :deep(.v-slide-group__next) {
        color: rgb(242, 204, 15);
        opacity: 0.6;

        &:hover {
            opacity: 1;
        }
    }

    :deep(.v-tab) {
        text-transform: none !important;
    }

    .link-to-out-of-blog {
        text-decoration: none;
        font-size: 1rem;
        font-weight: 800;
        transition: color 0.3s ease, transform 0.2s ease;
    }

    .link-to-out-of-blog:hover {
        color: #ffffff;
        text-decoration: underline;
        transform: scale(1.03);
    }

    .link-to-out-of-blog:focus {
        outline: 2px solid rgba(255, 90, 0, 0.25);
        outline-offset: 2px;
    }
</style>