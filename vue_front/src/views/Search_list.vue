<template>
	<div class='Search_Result'>
		<h1>Result Tara~~</h1>
		<div v-for='list in lists' :key='list.pk'>
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
				class='btn btn-sm btn-outline-success'
				>Load More
			</button>
		</div>
	</div>
</template>

<script>
import { apiService } from '@/common/api.service.js';

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
		}
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
		}
	},
	created() {
		this.getResults()
	}
}
</script>

<style>
</style>
