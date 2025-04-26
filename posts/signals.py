from django.dispatch import Signal, receiver
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from .models import Post
import logging

logger = logging.getLogger(__name__)

# Custom signals
post_updated = Signal()

@receiver(post_save, sender=Post)
def handle_post_created(sender, instance, created, **kwargs):
    cache.delete('all_posts')
    cache.delete_pattern('*blog_post_list*')
    
    action = 'created' if created else 'updated'
    logger.info(f"Post {action}: {instance.title}")
    logger.info(f"Cache cleared")

@receiver(post_delete, sender=Post)
def handle_post_deleted(sender, instance, **kwargs):
    cache.delete('all_posts')
    cache.delete_pattern('*blog_post_list*')
    
    logger.info(f"Post deleted: {instance.title}")
    logger.info(f"Cache cleared")

@receiver(post_updated)
def handle_post_update(sender, instance, **kwargs):
    cache.delete('all_posts')
    cache.delete_pattern('*blog_post_list*')
    
    logger.info(f"Post update notification: {instance.title}")
    logger.info(f"Cache cleared")
