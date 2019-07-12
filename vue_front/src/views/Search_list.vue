<template>
	<div class='Search_Result'>
		<Mov></Mov>
		<h1>Result Tara~~</h1>
		<div class='result_style'>
			<div class='chat' v-for='list in lists' :key='list.pk'>
				<h2>
					<router-link
						:to='{ name: "Detail", params: { tag: list.tag } }'
						class='list-link'>
						{{ list.title }}
					</router-link>
					{{ list.body }}
				</h2>
			</div>
			<div class='paging'>
				<p v-show='loadingLists'>...loading...</p>
				<button
					v-show='next'
					@click='getResults'
					class='btn btn-more'
					>Load More
				</button>
			</div>
		</div>
	</div>
</template>

<script>
import { apiService } from '@/common/api.service.js';
import Mov from '@/components/Move_Bar.vue'

export default {
	name: 'Search',
	props: {
		title: {
			type: String,
			required: true
		}
	},
	data() {
		return {
			lists: [],
			next: null,
			loadingLists: false,
			latte: require('../assets/latte.png')
		}
	},
	components: {
		Mov
	},
	methods: {
		getResults() {
			let endpoint = `/api/rest_back/?search=${this.title}`;
			if (this.next) {
				endpoint = this.next;
			}
			this.loadingLists = true;
			apiService(endpoint)
				.then(data => {
					this.lists.push(...data.results)
					this.loadingLists = false;
					if (data.next) {
						this.next = data.next;
					} else {
						this.next = null;
					}
				})
		},
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
	},
	created() {
		this.getResults()
	}
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Indie+Flower&display=swap');

.Search_Result h1 {
	font-family: 'Indie Flower', cursive;
	color: #BE800E;
}
.result_style {
	border: 4px double #BE800E;
	border-radius: 7px;
	width: 95%;
	height: 100%;
	position: relative;
	left: 2.5%;
	top: 15px;
}
</style>
