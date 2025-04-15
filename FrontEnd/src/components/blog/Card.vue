<template>
    <div class="card-container" :style="{ backgroundImage: `url(${encodeURI(bgImage)})` }" @click="$emit('click')">
        <div class="overlay">
            <div class="text-container">
                <h2 class="title-text">{{ title }}</h2>
            </div>

            <div class="footer-container">
                <!-- 日期 + 分类 -->
                <div class="info-row">
                    <span class="created-date">
                        <v-icon class="created-date-icon" icon="mdi-alarm" size="small" start></v-icon>
                        <span class="created-date-text">{{ createdDate }}</span>
                    </span>
                    <span class="category">
                        <v-icon class="category-icon" icon="mdi-bookmark-multiple"></v-icon>
                         <span class="category-text">{{ category }}</span>
                    </span>
                </div>

                <!-- 分割线 -->
                <div class="divider"></div>

                <!-- tags -->
                <div class="tags">
                    <template v-for="tag in tags" :key="tag.name">
                        <span class="tag">
                            <span class="tag-text">#{{ tag.name }}</span>
                        </span>
                    </template>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang='ts'>
    import type {Tag} from "@/store/blog/types/tag.ts";

    defineOptions({
        name: 'Card',
        inheritAttrs: false
    })

    defineProps<{
        title: string
        bgImage: string
        createdDate: string
        category: string
        tags: Tag[]
    }>()

</script>

<style scoped lang='scss'>
    .card-container {
        position: relative;
        width: 100%;
        max-width: 360px;
        height: 15rem;
        margin: 0 auto;
        border-radius: 5px;
        box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5);
        overflow: hidden;
        background-size: cover;
        background-position: center;
        display: flex;
        align-items: stretch;
        justify-content: flex-start;
        cursor: pointer;
        transition: transform 0.3s ease, box-shadow 0.3s ease;

        &:hover {
            transform: scale(1.05); // 放大 5%
            box-shadow: 8px 8px 15px rgba(0, 0, 0, 0.35);
            z-index: 1;
        }

        .overlay {
            background-image: linear-gradient(to bottom,
                rgba(0, 0, 0, 0.1) 0%,
                rgba(0, 0, 0, 0.2) 100%
            );
            width: 100%;
            padding: 16px;
            display: flex;
            flex-direction: column;
            gap: 8px;
            color: #ffffff;
            height: 100%;
        }

        .text-container {
            margin: 40px 10px 20px 10px;

            .title-text {
                margin: 0 0 10px 10px;
                font-size: 1.25rem;
                font-weight: bold;
                color: white;
            }
        }

        .footer-container {
            margin: auto 15px 5px 15px;

            .info-row {
                display: flex;
                justify-content: space-between;
                font-size: 0.7rem;

                .created-date {
                    color: white;
                    display: flex;
                    align-items: center;

                    .created-date-text {
                        font-size: 0.75rem;
                    }
                }

                .category {
                    color: white;
                    display: flex;
                    align-items: center;
                    gap: 2px;

                    .category-text {
                        font-size: 0.75rem;
                    }

                    .category-icon{
                        font-size: 0.75rem;
                    }
                }
            }

            .divider {
                height: 1.5px;
                background-color: rgba(255, 255, 255, 0.5);
                margin: 5px 0;
            }

            .tags {
                margin: 10px 0 0 0;
                display: flex;
                gap: 5px;

                .tag {
                    background: rgba(255, 255, 255, 0.2);
                    padding: 2px 5px;
                    border-radius: 4px;
                    font-size: 0.65rem;
                }
            }
        }
    }
</style>
