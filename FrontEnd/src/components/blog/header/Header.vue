<template>
    <div class="header-container"
         :class="{'change-bgcolor':coverImage.isScrollOverViewport}">
        <div class="title-big">
            <HeaderTitle></HeaderTitle>
        </div>
        <div class="nav-big">
            <HeaderNav></HeaderNav>
        </div>
        <div class="widget-big">
            <HeaderWidget></HeaderWidget>
        </div>
    </div>
</template>

<script setup lang='ts'>
    import HeaderNav from "@/components/blog/header/HeaderNav.vue";
    import HeaderTitle from "@/components/blog/header/HeaderTitle.vue";
    import HeaderWidget from "@/components/blog/header/HeaderWidget.vue";
    import useAppearanceStore from "@/store/blog/storages/appearance.ts";

    defineOptions({
        name: 'Header',
        inheritAttrs: false
    })

    const coverImage = useAppearanceStore()
</script>

<style scoped lang='scss'>
    .header-container {
        display: flex;
        justify-content: center;
        align-items: stretch;
        height: 100%;
        width: 100%;
        background-color: rgba(100, 100, 100, 0.15);

        .title-big {
            width: 35%;
            height: 100%;
            padding-right: 30px;
        }

        .nav-big {
            width: 35%;
            height: 100%;
        }

        .widget-big {
            width: 30%;
            height: 100%;
        }
    }

    .change-bgcolor {
        background-color: rgba(0, 14, 16, 0.75);
        border-bottom: 1px solid rgba(0, 100, 100, 0.5);
    }

</style>