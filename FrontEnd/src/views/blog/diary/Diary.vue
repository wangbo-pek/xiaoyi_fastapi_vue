<template>
    <div class="container">
        <div class="diary-timeline">
            <v-timeline class="diary-timeline" align="start" line-color="rgba(255, 255, 255, 0.5)">
                <v-timeline-item
                    v-for="diary in diaryStore.diaryList"
                    :key="diary.coverImg"
                    :dot-color="diary.timelineColor.pointColor"
                    size="small"
                    fill-dot
                    @click="jumpToDiaryDetail(diary.diaryListId)"
                >
                    <template v-slot:opposite>
                            <div class="diary-date">
                            <v-chip class="diary-date-chip" variant="tonal" label
                                    :style="{color:diary.timelineColor.pointColor}">
                                {{ diary.createdTime }}
                            </v-chip>
                        </div>
                    </template>
                    <div class="diary-item" :style="{background:diary.timelineColor.pointColor, color:diary.timelineColor.textColor}" >
                        <div class="title-brief-container">
                            <p class="title-brief-text">
                                <span class="title-text">『{{ diary.title }}』</span>
                                ——
                                <span class="brief-text">{{ diary.brief }}</span>"
                            </p>
                        </div>
                        <div class="cover-container">
                            <v-img
                                class="cover"
                                cover
                                :src="diary.coverImg"
                            ></v-img>
                        </div>

                        <div class="tag-container">
                            <template v-for="tag in diary.tags">
                                <span class="tag-text">#{{ tag.name }}</span>
                            </template>
                        </div>
                    </div>
                </v-timeline-item>
            </v-timeline>
        </div>
    </div>
</template>

<script setup lang='ts'>
    import {onMounted, onUnmounted} from "vue";
    import useAppearanceStore from "@/store/blog/storages/appearance.ts";
    import useDiaryStore from "@/store/blog/storages/diary.ts";
    import {useRouter} from "vue-router";

    defineOptions({
        name: 'Diary',
        inheritAttrs: false
    })

    const $router = useRouter()
    let appearanceStore = useAppearanceStore()
    let diaryStore = useDiaryStore()

    const jumpToDiaryDetail = (diaryListId: number) => {
        $router.push({
            name: 'diaryDetail',
            params: {
                id: diaryListId
            }
        })
    }

    onMounted(() => {
        appearanceStore.isShowHomeCover = false
        appearanceStore.isScrollOverViewport = true
    })

    onUnmounted(() => {
        appearanceStore.isShowHomeCover = true
    })

</script>

<style scoped lang='scss'>

    .container {
        display: flex;
        justify-content: center;
        position: relative;
        margin-bottom: 100px;
        z-index: 1;

        .diary-timeline {
            position: relative;
            top: 2rem;
            padding: 30px 25px 25px 25px;
            transition: transform 0.3s ease;

            .diary-item {
                max-width: 400px;
                border-radius: 5px;
                padding: 20px;
                margin-bottom: 50px;
                box-shadow: 5px 5px 10px rgba(255, 255, 255, 0.05);
                cursor: pointer;
                transition: transform 0.3s ease, box-shadow 0.3s ease;

                &:hover {
                    transform: scale(1.05);
                    box-shadow: 5px 5px 10px rgba(255, 255, 255, 0.2);
                    z-index: 1;
                }

                .title-brief-container {
                    margin-bottom: 15px;

                    .title-brief-text {
                        text-align: left;
                        line-height: 1.2rem;

                        .title-text {
                            font-size: 0.9rem;
                            font-weight: 800;
                        }

                        .brief-text {
                            font-size: 0.9rem;
                            font-weight: 200;
                        }
                    }
                }

                .cover-container {
                    display: flex;
                    justify-content: center;

                    .cover {
                        border-radius: 10px;
                        border: 1px solid rgba(255, 255, 255, 0.2);
                        box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.25);
                        backdrop-filter: blur(10px);
                        background-color: rgba(255, 255, 255, 0.3);
                        filter: brightness(0.7) contrast(0.75) blur(1.5px) sepia(50%);
                    }

                    .cover:hover {
                        filter: none;
                    }
                }

                .tag-container {
                    margin: 10px 5px 0 15px;

                    .tag-text {
                        text-align: left;
                        font-size: 0.75rem;
                    }
                }
            }
        }
    }

    .diary-date-chip {
        font-size: 1rem;
        font-weight: 900;
    }

</style>