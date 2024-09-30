<script>
    export let title;
    export let links;
</script>

<div class="block rounded-lg bg-white shadow-lg dark:bg-neutral-700 text-center m-1 square-box">
    <a href={links}>
        <div class="p-6 flex-col items-center justify-between">
            <!-- Slot for custom SVG -->
            <div class="svg-container flex justify-center mb-4">
                <slot name="icon"></slot> <!-- Custom content slot for SVG -->
            </div>

            <!-- Title -->
            <h5 class="mb-2 text-xl font-bold tracking-wide text-neutral-800 dark:text-neutral-50">
                {title}
            </h5>
        </div>
    </a>
</div>

<style>
    .svg-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 1rem; /* Adjust spacing as needed */
    }

    /* Set the box to be square */
    .square-box {
        width: 200px; /* Set width */
        height: 200px; /* Set height to be the same as width to make it square */
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* Adjustments for responsive behavior */
    @media (max-width: 768px) {
        .square-box {
            width: 150px; /* Adjust for smaller screens */
            height: 150px;
        }
    }
</style>
