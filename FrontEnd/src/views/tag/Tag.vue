<template>
    <div class="tag-container">
        <div class="my-category-title">
            ——&nbsp;&nbsp;&nbsp;文章分类&nbsp;&nbsp;&nbsp;——
        </div>
        <div class="my-category-container">
            <div class="categories-chip">
                <template v-for="item in categoryStore.categoryList" :key="item.category">
                    <MyChip
                        :name="item.name"
                        :noteCount="item.categoryCount"
                        :color="bgColor"
                    ></MyChip>
                </template>
            </div>

            <!-- 柱状图 -->
            <div class="categoryChartRef" ref="categoryChartRef"></div>
        </div>

        <div class="my-tag-title">
            ——&nbsp;&nbsp;&nbsp;文章标签&nbsp;&nbsp;&nbsp;——
        </div>
        <div class="my-tag-container">
            <div class="tags-chip">
                <template v-for="item in tagStore.tagList" :key="item.tag">
                    <MyChip
                        :name="item.name"
                        :noteCount="item.tagCount"
                        :color="item.color"
                    ></MyChip>
                </template>
            </div>

            <!-- 词云在这里展示 -->
            <div class="tagWordCloudRef" ref="tagWordCloudRef"></div>
        </div>
    </div>
    <div class="placeholder"></div>
</template>

<script setup lang='ts'>
    import {nextTick, onMounted, onUnmounted, ref} from "vue";
    import useAppearanceStore from "@/store/appearance.ts";
    import useCategoryStore from "@/store/category.ts";
    import useTagStore from "@/store/tag.ts";
    import axios_server from "@/utils/axios_server.ts";
    import * as echarts from 'echarts'
    import 'echarts-wordcloud'
    import MyChip from "@/components/MyChip.vue";
    import type {TagWithCount} from "@/store/types/tag.ts";
    import type {CategoryWithCount} from "@/store/types/category.ts";

    defineOptions({
        name: 'Tag',
        inheritAttrs: false
    })

    let appearanceStore = useAppearanceStore()
    let categoryStore = useCategoryStore()
    let tagStore = useTagStore()

    const bgColor = '#ffa500'

    const categoryChartRef = ref<HTMLDivElement | null>(null)
    let categoryChart: echarts.ECharts | null = null
    const tagWordCloudRef = ref<HTMLDivElement | null>(null)
    let tagChart: echarts.ECharts | null = null

    const initCategoryChart = () => {
        if (!categoryChartRef.value) return

        const xData = categoryStore.categoryList.map((category:CategoryWithCount) => category.name)
        const seriesData = categoryStore.categoryList.map((category:CategoryWithCount) => ({
            value: category.categoryCount,
            itemStyle: {
                color: bgColor
            }
        }))

        categoryChart = echarts.init(categoryChartRef.value)

        categoryChart.setOption({
            xAxis: {
                type: 'category',
                data: xData
            },
            yAxis: {
                type: 'value'
            },
            series: [{
                type: 'bar',
                data: seriesData
            }]
        })

        categoryChart.resize()
    }
    const initTagWordCloud = () => {
        if (!tagWordCloudRef.value) return

        const data = tagStore.tagList.map((tag: TagWithCount) => ({
            name: tag.name,
            value: tag.tagCount,
            textStyle: {
                color: tag.color
            }
        }))

        tagChart = echarts.init(tagWordCloudRef.value)
        tagChart.setOption({
            series: [{
                type: 'wordCloud',
                shape: 'circle',
                sizeRange: [12, 40],
                rotationRange: [-90, 90],
                gridSize: 8,
                textStyle: {
                    fontFamily: 'sans-serif'
                },
                data: data
            }]
        })

        tagChart.resize()
    }

    onMounted(() => {
        appearanceStore.isShowHomeCover = false
        appearanceStore.isScrollOverViewport = true

        // 获取所有分类
        axios_server.get('/api/tag_category/categories').then(
            async (response) => {
                categoryStore.categoryList = response.data
                await nextTick()
                initCategoryChart()
            }
        ).catch(err => {
            console.error('获取分类出错', err)
        })

        // 获取所有标签
        axios_server.get('/api/tag_category/tags').then(
            async (response) => {
                tagStore.tagList = response.data
                await nextTick()
                initTagWordCloud()
            }
        ).catch(err => {
            console.error('获取标签出错', err)
        })
    })

    onUnmounted(() => {
        appearanceStore.isShowHomeCover = true

        if (categoryChart) {
            categoryChart.dispose()
            categoryChart = null
        }
    })
</script>

<style scoped lang="scss">
    .tag-container {
        position: relative;
        top: 1rem;

        .my-category-title {
            margin: 100px 0 30px 250px;
            text-align: left;
            color: white;
            font-size: 1.5rem;
            font-weight: 800;
        }

        .my-category-container {
            max-width: 85%;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            position: relative;
            left: 7rem;

            .categories-chip {
                position: relative;
                left: 3rem;
            }

            .categoryChartRef {
                width: 85%;
                height: 350px;
            }
        }

        .my-tag-title {
            margin: 20px 0 30px 250px;
            text-align: left;
            color: white;
            font-size: 1.5rem;
            font-weight: 800;
        }

        .my-tag-container {
            max-width: 85%;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            position: relative;
            left: 7rem;

            .tags-chip {
                position: relative;
                left: 3rem;
            }

            .tagWordCloudRef {
                background-color: rgba(255, 255, 255, 0.05);
                width: 70%;
                height: 400px;
                margin-top: 10px;
                margin-left: 60px;
            }
        }
    }

    .placeholder {
        margin-bottom: 50px;
    }
</style>