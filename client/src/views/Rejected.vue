<template>
    <div class="rejected">
        <div class="alert alert-danger">
            <strong>Your link is not correctly!</strong>
            <p class="mb-0">Sorry, but this link is not saved in our service</p>
        </div>

        <router-link :to="{ name: 'Index' }" class="btn">Back to home</router-link>
    </div>
</template>

<script>
export default {
    name: 'Rejected',
    metaInfo: {
      title: 'Rejected'
    },
}
</script>