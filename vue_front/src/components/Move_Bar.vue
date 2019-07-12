<template>
	<div class="Move_there">
		<div class="home_bar">
			<img :src="latte" v-on:click="home">
		</div>
		<div class="main_bar">
			<img :src="latte" v-on:click="main">
		</div>
	</div>
</template>

<script>
	export default {
		name: 'Mov',
		data() {
			return{
				latte: require('../assets/latte.png')
			}
		},
		methods: {
			home() {
				this.$router.push({
					name: 'Thumnail'
				})
			},
			main() {
				this.$router.push({
					name: 'Main'
				})
			}

		}
	}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Indie+Flower&display=swap');

.Move_there {
	position: absolute;
	right: 10%;
}
.Move_there img {
	width: 50px;
	left: 40%;
	cursor: pointer;
}
.home_bar {
	position: absolute;
	padding: 5px;
	right: 10%;
}
.main_bar {
	position: absolute;
	padding: 5px;
}
</style>

